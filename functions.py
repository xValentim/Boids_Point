import pygame
import random
from values import *

max_dots = 50

def to_draw_vehicle_picture(v1, vehicles, window):
    health_i = round(v1.health) + 1
    if health_i < 1:
        health_i = 1
    elif health_i > 7:
        health_i = 7
    k = float(v1.r)
    vehicles[health_i] = pygame.transform.scale(vehicles_base[health_i], (int(k * 30), int(k * 16)))

    teta = v1.velocity.as_polar()
    teta = teta[1]
    
    vehicles[health_i] = pygame.transform.rotate(vehicles[health_i], -teta)
    
    rect = vehicles[health_i].get_rect()
    rect.center = v1.position
    
    window.blit(vehicles[health_i], rect)

def to_draw_vehicle_polygon(v1, window):
    max_speed = v1.maxspeed
    k = v1.velocity.magnitude_squared() / (max_speed * max_speed)
    teta = int(110 + k * 50)
    p1 = v1.position +  v1.velocity.normalize() * 12
    p2 = v1.position + (v1.velocity.normalize() * 6).rotate(teta)
    p3 = v1.position + (v1.velocity.normalize() * 6).rotate(-teta)
    alfa = 1
    if alfa <= 0:
        alfa = 0
    R = int(255 * (1 - alfa))
    G = int(255 * alfa)
    B = 0
    cor = (R, G, B)
    #print(cor)
    pygame.draw.polygon(window, cor, [p1, p2, p3])
    pygame.draw.polygon(window, cor, [p1, p2, p3], 1)


def texto(window, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])