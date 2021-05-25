#imports the pygame module with all functions and classes
import pygame

pygame.init()
clock = pygame.time.Clock()
#the code for your game has to go between these two lines

#create a window object
window = pygame.display.set_mode((640,480))
space = pygame.Rect(30,30,100,50)
Boom = pygame.Rect(230,30,100,50)
Ship = pygame.image.load('ship.png')
#create a game loop
running = True #game state
  #color the window background
Color = (130, 252, 100)
Color2 = (0,0,100)
Black = (0,0,0)
window.fill((Black))
Left  = (-5, 0)
Right = (5, 0)
Up    = (0, -5)
Down  = (0, 5)
direction = (0,0)
rect  = False
Ship = pygame.image.load('ship.png').convert_alpha()
Ship = pygame.transform.scale(Ship, (50, 50))         
space = Ship.get_rect()
        
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
              # pygame.draw.rect(window,Color, space)
              pygame.draw.rect(window,Color2, Boom)
              rect = True
            elif rect and event.key == pygame.K_RETURN:
               rect = False 
            #moves the object in a direction                    
            elif event.key == pygame.K_w and rect:
              direction = Up
            elif event.key == pygame.K_s and rect:      
              direction = Down   
            elif event.key == pygame.K_a and rect:  
              direction = Left
            elif event.key == pygame.K_d and rect: 
              direction = Right
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #if a mouse button event happened do this
            #get the position of the mouse
          mouse_position = event.pos
            #change the position of the rectangle
          Boom.center = mouse_position
        if event.type == pygame.KEYUP: 
          if event.key == pygame.K_w and direction == Up:   
           direction = (0,0)
          if event.key == pygame.K_a and direction == Left:
            direction = (0,0)
          if event.key == pygame.K_s and direction == Down:
            direction = (0,0)
          if event.key == pygame.K_d and direction == Right:
            direction = (0,0)
           #does not work as intended, stops even if its a random key.
    
    if space.colliderect(Boom):
      Color = (255,0,10)
      Color2 = (100,0,0)
    space.move_ip(direction)
    window.fill((Black))
    clock.tick(30)
    if rect:
      window.blit(Ship,space)
      pygame.draw.rect(window,Color2, Boom)
        #update the display
      pygame.display.update()
      Color = (130, 252, 100)
      Color2 = (0,0,100)
#this code will only run when the loop is stopped
pygame.quit()