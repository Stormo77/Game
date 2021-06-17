import pygame
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
#Values for Screen
HEIGHT = 450
WIDTH = 400
#Physics
ACC = 0.5
FRIC = -0.12
#Fps
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
     super().__init__()
     self.surf = pygame.Surface((30,30))
     self.surf.fill ((128,255,40))
     self.rect = self.surf.get.rect(center = (10,420))
        
class platform(pygame.sprite.Sprite):
    def __init__(self) -> None:
     super().__init__()
     self.surf = pygame.Surface((WIDTH,20))
     self.surf.fill((255,0,0))
     self.rect = self.surf.get.rect(center = (WIDTH/2, HEIGHT -10))
   
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC   
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc            


PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    displaysurface.fill((0,0,0))
    
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        
    pygame.display.update()
    FramePerSec.tick(FPS)        
