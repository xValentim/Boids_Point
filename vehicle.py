#from hashlib import new
import pygame
import math
import random
from values import *

def position_average(vehicles_list):
    n = len(vehicles_list)
    mid_point = pygame.Vector2()
    for boid in vehicles_list:
        mid_point += boid.position
    mid_point /= n
    return mid_point

def velocity_average(vehicles_list):
    n = len(vehicles_list)
    mid_velocity = pygame.Vector2()
    for boid in vehicles_list:
        mid_velocity += boid.velocity
    mid_velocity /= n
    return mid_velocity

def create_vehicles(n):
    return [Vehicle(random.randint(1, largura), random.randint(1, altura)) for i in range(n)]

class Vehicle:
    def __init__(self, x=0 , y=0, dna=[], flag_predator=False):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.acceleration = pygame.Vector2()
        self.radius_cohesion = 50
        self.radius_alignment = 30
        self.radius_separation = 50
        self.r = 0.8
        self.maxforce = 0.3
        self.maxspeed = 2

    def limit(self, limit_value, vector):
        if vector.magnitude_squared() > limit_value * limit_value:
            return (vector.normalize()) * limit_value
        else:
            return vector
    
    def alignment(self, vehicles_list):
        boids = []
        Radius_max_2 = self.radius_alignment * self.radius_alignment
        for v in vehicles_list:
            d_2 = (v.position - self.position).magnitude_squared()
            if d_2 < Radius_max_2:
                boids.append(v)
        target = velocity_average(boids)
        '''if len(boids) > 0:
            target = velocity_average(boids)
        else:
            target = self.velocity'''
        target = target.normalize() * self.maxspeed
        steering = target - self.velocity
        self.applyForce(steering / 5)

    def cohesion(self, vehicles_list):
        boids = []
        Radius_max_2 = self.radius_cohesion * self.radius_cohesion
        for v in vehicles_list:
            d_2 = (v.position - self.position).magnitude_squared()
            if d_2 < Radius_max_2:
                boids.append(v)
        target = position_average(boids)
        if target != self.position:
            desire = (self.position - target).normalize() * self.maxspeed
            steering = self.velocity - desire
        else:
            steering = pygame.Vector2()
        self.applyForce(steering / 2)
    
    def separation(self, vehicles_list):
        boids = []
        Radius_max_2 = self.radius_separation * self.radius_separation
        for v in vehicles_list:
            d_2 = (v.position - self.position).magnitude_squared()
            if d_2 < Radius_max_2:
                boids.append(v)
        target = position_average(boids)
        if target != self.position:
            desire = (self.position - target).normalize() * self.maxspeed
            steering = self.velocity - desire
            D = (target - self.position).magnitude()
        else:
            steering = pygame.Vector2()
            D = 1
        
        self.applyForce(-steering * 8 / (D))
    
        
    # Update location
    def update(self, vehicles_list):
    
        # Boundary condition (depende da aceleração)
        self.boundary()

        self.cohesion(vehicles_list)
        self.separation(vehicles_list)
        self.alignment(vehicles_list)

        # Update velocity
        self.velocity += self.acceleration

        # Limit is maxspeed
        self.velocity = self.limit(self.maxspeed, self.velocity)

        # Update location with new velocity
        self.position += self.velocity

        # Boundary condition (depende da posição)
        #self.periodic_boundary()
        
        # Set zero acceleration
        self.acceleration = self.acceleration * 0

    def boundary(self):
        d = 15
        desired = pygame.Vector2()
        if self.position.x < d:
            desired = pygame.Vector2(self.maxspeed, self.velocity.y)
        elif self.position.x > largura - d:
            desired = pygame.Vector2(-self.maxspeed, self.velocity.y)
        if self.position.y < d:
            desired = pygame.Vector2(self.velocity.x, self.maxspeed)
        elif self.position.y > altura - d:
            desired = pygame.Vector2(self.velocity.x, -self.maxspeed)

        if desired.magnitude_squared() > 0:
            desired = desired.normalize() * self.maxspeed
            steer = desired - self.velocity
            steer = self.limit(self.maxforce, steer)
            self.applyForce(steer)
    
    def periodic_boundary(self):
        self.position.x = self.position.x % largura
        self.position.y = self.position.y % altura

    def applyForce(self, force):
        self.acceleration += self.limit(self.maxforce, force)
    
    def seek(self, target):
        # Calculate desired
        desired = target - self.position
        desired = desired.normalize() * self.maxspeed

        # Calculate steer (Craig Raynolds classic vehicle)
        # steering = desired - velocity
        steer = desired - self.velocity

        # Limit steer
        steer = self.limit(self.maxforce, steer)

        return steer
