#from hashlib import new
import pygame
import math
import random
from values import *

class Vehicle:
    def __init__(self, x=0 , y=0, dna=[], flag_predator=False):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.acceleration = pygame.Vector2()
        self.radius_cohesion = 30
        self.radius_alignment = 30
        self.radius_separation = 30
        self.r = 0.8
        self.maxforce = 0.2
        self.maxspeed = 4

    def limit(self, limit_value, vector):
        if vector.magnitude_squared() > limit_value * limit_value:
            return (vector.normalize()) * limit_value
        else:
            return vector

    def cohesion():
        pass

    # Update location
    def update(self):
    
        # Boundary condition (depende da aceleração)
        self.boundary()

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
        self.acceleration += force
    
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
def create_vehicles(n):
    return [Vehicle(random.randint(1, largura), random.randint(1, altura)) for i in range(n)]