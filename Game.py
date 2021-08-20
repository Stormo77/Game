#imports the pygame module with all functions and classes
import pygame
from pygame.locals import *
import random
from enum import Enum
import time
from pygame.time import Clock, wait
vec = pygame.math.Vector2

pygame.init()
clock = pygame.time.Clock()

#Numbers converted to names
height = 480
width = 640
zero = 0
#colors for game
black = (0,0,0)
white = (255,255,255)
#frames
fps = 60
win = False
#time
start_time = time.time()
game_duration = 120
#game states for gameover, menu and running
class EGameState(Enum):
  gsmenu = 1
  gsrunning = 2
  gsgameover = 3
  gsgameending = 4

GameState = EGameState.gsmenu
#Classes for game
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.identity = False
        self.dead = False
    def move(self, direction):
        #self.move_ip = direction
        if direction == 'left':
            self.pos.x += -2.5
        elif direction == 'right':
            self.pos.x += +2.5
        elif direction == 'up':
            self.pos.y += -2.5
        elif direction == 'down':
            self.pos.y += +2.5
        #Makes Screen have a border that the Sprites cannot cross   
        if self.pos.x - self.rect.width  / 2 <= zero:
          self.pos.x = self.rect.width  / 2
          
        if self.pos.x + self.rect.width / 2 >= width:
          self.pos.x = width - self.rect.width / 2
          
        if self.pos.y - self.rect.height /2 <= zero:
          self.pos.y = self.rect.height / 2
          
        if self.pos.y + self.rect.height /2 >= height:
          self.pos.y = height- self.rect.height /2
            
        #code for debuging movement      
        self.rect.center = self.pos
        #print(self.rect.center)
        #print(self.pos)
        #print(self.pos.x - self.rect.width /2)
        
        
   #for endgame text and clock
def displaytext(window,message,x,y):
  font = pygame.font.Font("freesansbold.ttf",32)
  renderedtext = font.render(message,True,white)
  textRect = renderedtext.get_rect()
  textRect.center =(x, y)
  window.blit(renderedtext,textRect)
#show who wins game
def showwin(window,message,x,y):
  font = pygame.font.Font("freesansbold.ttf",32)
  renderedtext = font.render(message,True,white)
  textRect = renderedtext.get_rect()
  textRect.center =(x, y)
  window.blit(renderedtext,textRect)   
 
      
class Enemy(MySprite):
    def __init__(self):
        super().__init__()
        image =  pygame.image.load('Ship.png') 
        self.surf = image
        self.pos = pygame.math.Vector2((550,400))
        self.rect = self.surf.get_rect(center = self.pos)
    def reset(self):
        self.pos = pygame.math.Vector2((550,400))
        self.rect = self.surf.get_rect(center = self.pos)          
    def process(self):
       pressed_keys = pygame.key.get_pressed()
       if pressed_keys[K_LEFT]:
        self.move('left') 
       if pressed_keys[K_RIGHT]:
        self.move('right') 
       if pressed_keys[K_UP]:
        self.move('up') 
       if pressed_keys[K_DOWN]:
        self.move('down') 
         
        
class Player(MySprite):
    def __init__(self):
        super().__init__()
        self.surf =pygame.image.load('Rock.png')
        self.pos = pygame.math.Vector2((100,100))
        self.rect = self.surf.get_rect(center = self.pos)          
    def reset(self):
        self.pos = pygame.math.Vector2((100,100))
        self.rect = self.surf.get_rect(center = self.pos)          
    def process(self):
       pressed_keys = pygame.key.get_pressed()
       if pressed_keys[K_a]:
        self.move('left') 
       if pressed_keys[K_d]:
        self.move('right') 
       if pressed_keys[K_w]:
        self.move('up') 
       if pressed_keys[K_s]:
        self.move('down')          
        
running = True #game state 
game_over_at = 0

def process(sprites, P1, P2):
    global running
    global GameState
    global game_over_at
    global start_time
    list_of_events = pygame.event.get()
    #debug code
    #print(GameState)
    
    if GameState != EGameState.gsgameending:
      for entity in sprites:
        entity.process()
      
    #loop through each event in the list
    for event in list_of_events:
        # print each event to console for debuging
        if event.type == pygame.QUIT:
            #exit the game if x in the corner clicked
            running = False
        elif event.type == pygame.KEYDOWN:
            #if a key gets pressed
            if event.key == pygame.K_ESCAPE:
                #if the escape key is pressed quit the game.
                running = False
            #moves the object in a direction                    
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                if GameState == EGameState.gsmenu:
                    GameState = EGameState.gsrunning
                    start_time = time.time()
    if GameState == EGameState.gsgameending and time.time() - game_over_at > 10:
          reset_game_state()
          #code for debug
          #print('game state reset')
          
    if time.time() - start_time > game_duration and GameState != EGameState.gsgameending:
      game_over()    
      #GameState = EGameState.gsgameover   
      #code for debug                 
      #print('Game over state set')
#code for starting menu to display title page
def rendermenu(window):
    BackgroundImage = pygame.image.load("TitlepageGame.png") 
    window.blit(BackgroundImage,(0,0))
#code for game running     
def renderrunning(sprites, window):
  for entity in sprites:
    window.blit(entity.surf,entity.rect) 
  #part of code for clock
  timelapsed = round(time.time()-start_time)
  timeremaining = game_duration - timelapsed
  displaytext(window, str(timeremaining),width//2,25)
 #code for game over   
def rendergameover(window):
    global win
    BackgroundImage = pygame.image.load("Gameoverpage.png") 
    window.blit(BackgroundImage,(0,0))
    if win ==True:
     showwin(window, 'Humanity win',width//2,300)
    else:
     showwin(window, 'Alien win',width//2,300)
    
    
    
#code to set the gamestate and what window is what   
def render(sprites, window):
  window.fill((black))
  if GameState == EGameState.gsrunning:
    renderrunning(sprites, window)
  elif GameState == EGameState.gsgameending:
      rendergameover(window)
  elif GameState == EGameState.gsmenu:
      rendermenu(window)   
 #to reset the game so you dont have to restart game again to play     
def reset_game_state():
  global start_time
  global GameState
  start_time = time.time()
  P1.reset()
  P2.reset()
  GameState = EGameState.gsmenu

#sprites and group for sprite
P1 = Player()
P2 = Enemy()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
 #code for the window's title and the display mode 
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evaders")  
#fill window
window.fill((black))
#game over feature, helps resets game
def game_over():
    global GameState
    global game_over_at
    global win
    #code for debug
    #print('Game Over')
    GameState = EGameState.gsgameending
    game_over_at = time.time()

#game loop
while running:
    
    process(all_sprites, P1, P2)  
    render(all_sprites, window)
    #update the display
    if GameState != EGameState.gsgameending:
      endgame = pygame.sprite.collide_rect(P1, P2)
      if endgame:
       win= True
      if endgame or GameState == EGameState.gsgameover:
        game_over()  
    pygame.display.update()
    clock.tick(fps)
if running  == False:
      
#this code will only run when the loop is stopped
 pygame.quit()
