#imports the pygame module with all functions and classes
import pygame

pygame.init()
#the code for your game has to go between these two lines

#create a window object
window = pygame.display.set_mode((640,480))
MyRect = pygame.Rect(30,30,100,50)
#create a game loop
running = True #game state
  #color the window background
window.fill((0,0,0))
rect = False
while running:
    #get all events that have happened since last loop
    list_of_events = pygame.event.get()
    #loop through each event in the list
    for event in list_of_events:
        #print each event to console for debuging
        print(event)
        if event.type == pygame.QUIT:
            #exit the game if x in the corner clicked
            running = False
        elif event.type == pygame.KEYDOWN:
            #if a key gets pressed
            if event.key == pygame.K_ESCAPE:
                #if the escape key is pressed quit the game.
                running = False
            if event.key == pygame.K_g and not rect:
              pygame.draw.rect(window,(130, 252, 100), MyRect)
              rect = True
            elif rect and event.key == pygame.K_g:
               window.fill((0,0,0))  
               rect = False                       
            if event.key == pygame.K_w:
                pass     
            elif event.key == pygame.K_s:  
                pass 
            elif event.key == pygame.K_a:  
                pass 
            elif event.key == pygame.K_d:  
                pass      
    #update the display
    pygame.display.update()

#this code will only run when the loop is stopped
pygame.quit()