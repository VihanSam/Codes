import pygame
import os
import time
import random
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#load images
RED_SPACE_SHIP = pygame.image.load("/Users/vihan/Desktop/Space invaders/assets/pixel_laser_red.png")
GREEN_SPACE_SHIP = pygame.image.load("/Users/vihan/Desktop/Space invaders/assets/pixel_laser_green.png")
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#player ship 
YELLOW_SPACE_SHIP = pygame.image.load("/Users/vihan/Desktop/Space invaders/assets/pixel_ship_yellow.png")

#laser
RED_LASER  = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER  = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER  = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER  = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# background color
BG = pygame.image.load(os.path.join("assets", "background-black.png"))

def main():
    run = True
    FPS = 60
    CLOCK  = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()