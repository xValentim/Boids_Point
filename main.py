import pygame
#from init_screen import *
from vehicle import *
from values import *
from functions import *

pygame.init()

t_major = 0
v_major = Vehicle(0, 0)
relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Evolutionary Steering Behaviors")
window.fill(gray)
#continua = init_screen(window, relogio)
continua = True
vehicles_list = create_vehicles(100)

while continua and number_of_generation <= max_generation:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
            if event.key == pygame.K_l:
                fps -= 60
            if event.key == pygame.K_s:
                fps += 60
             
    window.fill(gray)

    t += 1

    i = 0
    while i < len(vehicles_list):
        v1 = vehicles_list[i]
        v1.update()
        to_draw_vehicle_polygon(v1, window)
        i += 1

    relogio.tick(fps)
    pygame.display.update()

pygame.quit()