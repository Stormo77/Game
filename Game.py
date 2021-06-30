#imports the pygame module with all functions and classes
import pygame
from pygame.locals import *
import random
vec = pygame.math.Vector2

pygame.init()
clock = pygame.time.Clock()
#the code for your game has to go between these two lines

#create a window object
space = pygame.Rect(300,0,0,0)
boom = pygame.Rect(300,0,0,0)
ship = pygame.image.load('Ship.png')
rock = pygame.image.load('Rock.png')
#create a game loop
running = True #game state
  #color the window background
height = 480
width = 640
#colors for game
color = (130, 252, 100)
color2 = (0,0,100)
black = (0,0,0)
#Code for the direction that the objects move.
left  = (-5, 0)
right = (5, 0)
up    = (0, -5)
down  = (0, 5)
direction = (0,0)
direction2 = (0,0)
rect  = False
acc = 0.5
fric = -0.12
fps = 60
FramePerSec = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.identity = False
        self.surf =pygame.image.load('Ship.png')
        self.dead = False
        self.pos = pygame.math.Vector2((550,400))
        self.rect = self.surf.get_rect(center = self.pos)
    def move(self, direction):
        self.move_ip = direction
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf =pygame.image.load('Rock.png')
        self.rect = self.surf.get_rect()
        self.dead = False
        self.identity = False
P1 = Player()
P2 = Enemy()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)


ship = pygame.image.load('ship.png')
ship = pygame.transform.scale(ship, (150, 150))         
space = ship.get_rect()
dead = False

rock = pygame.image.load('Rock.png')
rock = pygame.transform.scale(rock, (150, 150))         
boom = rock.get_rect()
boom.move_ip (500,400) 
  
  
  
  
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alien Invaders")  
#fill window
window.fill((black))
  
while running:
    list_of_events = pygame.event.get()
    #loop through each event in the list
    for event in list_of_events:
        #print each event to console for debuging
        print(event)
        pygame.mouse.get_rel()
        pygame.mouse.set_visible(True)
        if event.type == pygame.QUIT:
            #exit the game if x in the corner clicked
            running = False
        elif event.type == pygame.KEYDOWN:
            #if a key gets pressed
            if event.key == pygame.K_ESCAPE:
                #if the escape key is pressed quit the game.
                running = False
            if event.key == pygame.K_RETURN and not rect:
              # pygame.draw.rect(window,Color, space)
              dead = False
              rect = True
              identity = True
              space.topleft = (0,0)
              boom.bottomright = (640,480)
            elif rect and event.key == pygame.K_RETURN:
               rect = False
               identity = False 
            #moves the object in a direction                    
            elif event.key == pygame.K_w and rect:
              direction = up
            elif event.key == pygame.K_s and rect:      
              direction = down   
            elif event.key == pygame.K_a and rect:  
              direction = left 
            elif event.key == pygame.K_d and rect: 
              direction = right
           #moves the Boom Object
           #moves the object in a direction                    
            elif event.key == pygame.K_UP and rect and not Dead:
              direction2 = up
            elif event.key == pygame.K_DOWN and rect and not Dead:      
              direction2 = down   
            elif event.key == pygame.K_LEFT and rect and not Dead:  
              direction2 = left
            elif event.key == pygame.K_RIGHT and rect and not Dead: 
              direction2 = right 
                 
        #elif event.type == pygame.MOUSEMOTION:
        
            #if a mouse button event happened do this
            #get the position of the mouse
            
          #mouse_position = event.pos
           
            #change the position of the rectangle
            
          #Crash.center = mouse_position
        if event.type == pygame.KEYUP: 
          if event.key == pygame.K_w and direction == up:   
           direction = (0,0)
          if event.key == pygame.K_a and direction == left:
            direction = (0,0)
          if event.key == pygame.K_s and direction == down:
            direction = (0,0)
          if event.key == pygame.K_d and direction == right:
            direction = (0,0)
          
          if event.key == pygame.K_UP and direction2 == up:   
           direction2 = (0,0)
          if event.key == pygame.K_LEFT and direction2 == left:
            direction2 = (0,0)
          if event.key == pygame.K_DOWN and direction2 == down:
            direction2 = (0,0)
          if event.key == pygame.K_RIGHT and direction2 == right:
            direction2 = (0,0)
    
    for entity in all_sprites:
          window.blit(entity.surf,entity.rect)
    pygame.display.update()
  
    if boom.colliderect(space):
      Dead = True
    space.move_ip(direction)
    boom.move_ip(direction2)
    window.fill((black))
    clock.tick(30)
    if rect:
      if not Dead: window.blit(rock,boom)
      window.blit(ship,space)
        #update the display
      pygame.display.update()
      color = (130, 252, 100)
      color2 = (0,0,100)
   
    if space.top < 0: 
      space.bottom = 480
    if space.bottom > 480: 
      space.top = 0
     
    if space.left < 0: 
      space.right = 640
    if space.right > 640: 
      space.left = 0
      
      
    if boom.top < 0: 
     boom.bottom = 480
    if boom.bottom > 480: 
     boom.top = 0
     
    if boom.left < 0: 
      boom.right = 640
    if boom.right > 640: 
      boom.left = 0
    
#this code will only run when the loop is stopped
pygame.quit()
