#imports the pygame module with all functions
import pygame
pygame.init()
#code for game
window = pygame.display.set_mode((1280,720))
running = True #game state
while running:
    #events since last loop
    list_of_events = pygame.event.get()
    #loop through each event
    for event in list_of_events:
        print(event)
        if event.type == pygame.QUIT:
            running = False
window.fill((100,100,0))
print('hello')

pygame.display.update()
pygame.quit()

