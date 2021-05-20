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
Color = (130, 252, 100)
Black = (0,0,0)
window.fill((Black))
Left  = (-10, 0)
Right = (10, 0)
Up    = (0, -10)
Down  = (0, 10)
rect  = False
while running:
    #get all events that have happened since last loop
    list_of_events = pygame.event.get()
    #loop through each event in the list
    for event in list_of_events:
        #print each event to console for debuging
        print(event)
        pygame.mouse.get_rel()
        pygame.mouse.set_visible(True)
        pygame.display.update()

        if event.type == pygame.QUIT:
            #exit the game if x in the corner clicked
            running = False
        elif event.type == pygame.KEYDOWN:
            #if a key gets pressed
            if event.key == pygame.K_ESCAPE:
                #if the escape key is pressed quit the game.
                running = False
            if event.key == pygame.K_RETURN and not rect:
              pygame.draw.rect(window,Color, MyRect)
              rect = True
            elif rect and event.key == pygame.K_RETURN:
               rect = False 
            #moves the object in a direction                    
            elif event.key == pygame.K_w and rect:
              MyRect.move_ip   (Up)
            elif event.key == pygame.K_s and rect:      
              MyRect.move_ip (Down)   
            elif event.key == pygame.K_a and rect:  
              MyRect.move_ip (Left)
            elif event.key == pygame.K_d and rect: 
              MyRect.move_ip(Right)
              
  
        
        window.fill((Black))
        if rect:
          pygame.draw.rect(window,Color,MyRect) 
        #update the display
        pygame.display.update()
#this code will only run when the loop is stopped
pygame.quit()