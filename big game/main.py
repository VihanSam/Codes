# import pygame package
import pygame
  
# initializing imported module
pygame.init()
  
# displaying a window of height
# 500 and width 400
pygame.display.set_mode((800, 500))
surface = pygame.display.set_mode((800, 500))
color = ('white')
#Vars
X = 800
Y = 500

# Changing surface color
surface.fill(color)
pygame.display.flip()
# creating a bool value which checks
# if game is running
running = True
screen = pygame.display.set_mode((X, Y))

#Sprite_load
imp = pygame.image.load("/Users/vihan/Documents/big game/graphics/test/player.png")
 
#Caption
pygame.display.set_caption('Pygame window')

screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()
status = True
while (status):

# keep game running till running is true
    while running:
      
    # Check for event if user has pushed
    # any event in queue
        for event in pygame.event.get():
          
        # if event is of type quit then 
        # set running bool to false
            if event.type == pygame.QUIT:
                running = False
            