import pygame
import random
from math import *

fps = 60
t_max = 1200
t = 0
total_life_time = 0
total_generation = 0
total_fitness = 0
total_dna = [0] * 6
number_of_generation = 0
max_generation = 1000
largura = 1020
altura = 600
tamanho_barra = 200
centro = pygame.Vector2(largura / 2, altura / 2)
dna_view = False

gray = (51, 51, 51)
gray2 = (41, 41, 41)
gray3 = (31, 31, 31)
gray4 = (11, 11, 11)
black = (0, 0, 0)
white = (255, 255, 255)
red = (250, 0, 0)
green = (0, 250, 0)
blue = (0, 0, 250)
cyan = (0, 15, 150)

vehicle_img = pygame.image.load("imgs_vehicles/vehicle_none.png")
vehicle_img0 = pygame.image.load("imgs_vehicles/vehicle_none.png")
vehicle_img1 = pygame.image.load("imgs_vehicles/vehicle_health1.png")
vehicle_img2 = pygame.image.load("imgs_vehicles/vehicle_health2.png")
vehicle_img3 = pygame.image.load("imgs_vehicles/vehicle_health3.png")
vehicle_img4 = pygame.image.load("imgs_vehicles/vehicle_health4.png")
vehicle_img5 = pygame.image.load("imgs_vehicles/vehicle_health5.png")
vehicle_img6 = pygame.image.load("imgs_vehicles/vehicle_health6.png")
vehicle_img7 = pygame.image.load("imgs_vehicles/vehicle_health7.png")
poison_img = pygame.image.load("imgs_vehicles/veneninho_vermelho.png")
food_img= pygame.image.load("imgs_vehicles/hamburguer.png")

vehicles_base = [
    vehicle_img0,
    vehicle_img7,
    vehicle_img6,
    vehicle_img5,
    vehicle_img4,
    vehicle_img3,
    vehicle_img2,
    vehicle_img1,
    vehicle_img1
]

vehicles = list(vehicles_base)



