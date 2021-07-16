from operator import pos
from tkinter import LEFT
import pygame
from values import *
from functions import *
from vehicle import *


# Centraliza retangulo
def create_rect(window, color, center, b, h):
    pygame.draw.rect(window, color, [center[0] - b / 2, center[1] - h / 2, b, h])
    return None

# Tela inicial
def init_screen(window, relogio):
    vehicles_list = create_vehicles(25)

    init_sc = True
    while init_sc:
        target = pygame.mouse.get_pos()
        pos_mouse = pygame.Vector2(target[0], target[1])
        distancia_ao_centro = (pos_mouse - centro).magnitude()
        pygame.draw.circle(window, green, centro, 20)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if distancia_ao_centro < 20 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True
            if (pos_mouse - pygame.Vector2(largura / 2, altura / 2 + 45)).magnitude() < 20 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return False
        window.fill(gray)

        
        texto(window, f"Start", white, 30, largura / 2 - 25, altura / 2 - 12)
        if distancia_ao_centro < 20:
            create_rect(window, gray3, [largura / 2, altura / 2], 140, 40)
            texto(window, f"Start", green, 30, largura / 2 - 25, altura / 2 - 10)

        texto(window, f"Quit", white, 30, largura / 2 - 25, altura / 2 + 37)
        if (pos_mouse - pygame.Vector2(largura / 2, altura / 2 + 45)).magnitude() < 20:
            create_rect(window, gray3, [largura / 2, altura / 2 + 45], 140, 40)
            texto(window, f"Quit", red, 30, largura / 2 - 25, altura / 2 + 35)
            
        for v in vehicles_list:
            v.behaviors([pos_mouse], [], [])
            v.update()
            v.dna[3], v.dna[4], v.dna[5] = 200, 200, 200
            v.health = 4
            v.maxforce = 0.1
            v.maxspeed = 5
            to_draw_vehicle_polygon(v, window)

        relogio.tick(fps)
        pygame.display.update()
        
        

