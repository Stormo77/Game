#import the modules that we will use in the game
import pygame
import random

#initalise the pygame module
pygame.init()

#configuration variables

#if running is True then the loop will continue
#if running is False then the loop will end
running  = True
#screen
HEIGHT = 600
WIDTH = 800

#code for?
recent_events = pygame.event.get()

#frame rate of the game
FPS = 60

#create the game Clock object
game_clock = pygame.time.Clock()

"""
Here is where you define all your
- game objects/classes
- game methods/functions

This will be one of the largest sections of your code
when your game is complete.
"""

#create the game wd with a name in the top bar
wd = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Repel The Alien Invader")

"""
Here is where you put all your game initialisation code
- the creation of game objects
    - the window
    - the Clock
    - Sprites
        - the Player
        - Platforms etc
    - sprite Groups
- placing objects in the game
- drawing the initial game level
"""
class ship(pygame.sprite.Sprite):
    #player object which inherits from Sprite
    def __init__(self,position):
        #initialises the object when it is first created
        super().__init__()
        #ship sprite image and rectangle
        self.surf = pygame.image.load("ship.png")
        self.surf = pygame.transform.scale(self.surf,(30,30))
        self.rect = self.surf.get_rect(center = position)
        #ship physics
        self.pos = pygame.math.Vector2(position)
        self.vel = pygame.math.Vector2((0,0))
        self.acc = pygame.math.Vector2((0,0))
        #ship stats
        self.health = 100
        self.armor = 0
    
    def move(self):
        #code for ship movement goes here
        pass
    def update(self):
        #code for updating the ship position
        #and anything else that needs to happen
        #every game tick goes here
        pass

#the main game loop
while running:

    #controling the framerate with the game clock
    game_clock.tick(FPS)
    #section 1
    """
    Here is where you code your main event loop for
    -key presses
    -mouse movement and button clicks
    Code here should use a lot of if, elif, and else
    statements to react in different ways based on 
    user input
    """
    for event in recent_events:
        if event.type == pygame.QUIT:
         running = False
        elif event.type == pygame.KEYDOWN:
        #if a key is pressed check which key
         if event.key == pygame.K_ESCAPE:
            running = False
        elif event.key == pygame.K_SPACE:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
         if event.button == pygame.BUTTON_LEFT:
            #code here for when the left mouse button is pressed
            pass
        
    #section 2
    """
    Here is where all the code that happens after the events.
    This code will run every loop and doesn't depend on user input.
    This will have code for
    - updating movement of sprites
    - detecting colisions between sprites
    - killing/removing sprites that are no longer needed
    - creating new sprites if needed
    - drawing all objects on to the display before updating
    """
    #updating the display should happen at the end of the loop
    pygame.display.update()
    #loops back to the start from here
"""
Here is where you will have all the code that 
happens after the main game loop is finished. 
At a minimum it will be pygame quit to close the program.
"""
pygame.quit()
