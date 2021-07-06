#imports the pygame module with all functions and classes
import pygame
from pygame.locals import *
import random

from pygame.time import Clock
vec = pygame.math.Vector2

pygame.init()
clock = pygame.time.Clock()

#color the window background
height = 480
width = 640
#colors for game
black = (0,0,0)
#Code for the direction that the objects move.
fps = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.identity = False
        self.surf =pygame.image.load('Ship.png')
        self.dead = False
        self.pos = pygame.math.Vector2((550,400))
        self.rect = self.surf.get_rect(center = self.pos)
    def move(self, direction):
        #self.move_ip = direction
        if direction == 'left':
            self.pos.x += -10
        elif direction == 'right':
            self.pos.x += +10
        elif direction == 'up':
            self.pos.y += -10
        elif direction == 'down':
            self.pos.y += +10
        self.rect.center = self.pos
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf =pygame.image.load('Rock.png')
        self.rect = self.surf.get_rect()
        self.dead = False
        self.pos = pygame.math.Vector2((100,100))
        self.rect = self.surf.get_rect(center = self.pos)
        self.identity = False
    def move(self, direction):
      if direction == 'left':
        self.pos.x += -10
      elif direction == 'right':
        self.pos.x += +10
      elif direction == 'up':
        self.pos.y += -10
      elif direction == 'down':
        self.pos.y += +10
      self.rect.center = self.pos
P1 = Player()
P2 = Enemy()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
  
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alien Invaders")  
#fill window
window.fill((black))

#game loop
running = True #game state 
while running:
    list_of_events = pygame.event.get()
    #loop through each event in the list
    for event in list_of_events:
        #print each event to console for debuging
        if event.type == pygame.QUIT:
            #exit the game if x in the corner clicked
            running = False
        elif event.type == pygame.KEYDOWN:
            #if a key gets pressed
            if event.key == pygame.K_ESCAPE:
                #if the escape key is pressed quit the game.
                running = False
            #moves the object in a direction                    
            elif event.key == pygame.K_w:
              P1.move('up')
            elif event.key == pygame.K_s:      
              P1.move('down')  
            elif event.key == pygame.K_a:  
              P1.move('left') 
            elif event.key == pygame.K_d: 
              P1.move('right')
           #moves the Boom Object
           #moves the object in a direction                    
            elif event.key == pygame.K_UP:
              P2.move('up')
            elif event.key == pygame.K_DOWN:      
              P2.move('down')  
            elif event.key == pygame.K_LEFT:  
              P2.move('left')
            elif event.key == pygame.K_RIGHT: 
              P2.move('right')
    
    window.fill((black))
    for entity in all_sprites:
          window.blit(entity.surf,entity.rect)
    #update the display
    endgame = pygame.sprite.collide_rect(P1, P2)
    if endgame:
      print('hello')
      running = False
          
    pygame.display.update()
    
    clock.tick(fps)
   
    # if space.top < 0: 
    #   space.bottom = width
    # if space.bottom > width: 
    #   space.top = 0
     
    # if space.left < 0: 
    #   space.right = height
    # if space.right > height: 
    #   space.left = 0
      
      
    # if boom.top < 0: 
    #  boom.bottom = width
    # if boom.bottom > width: 
    #  boom.top = 0
     
    # if boom.left < 0: 
    #   boom.right = height
    # if boom.right > height: 
    #   boom.left = 0
if running  == False:
      
#this code will only run when the loop is stopped
pygame.quit()
