#imports the pygame module with all functions and classes
import pygame

pygame.init()
clock = pygame.time.Clock()
#the code for your game has to go between these two lines

#create a window object
window = pygame.display.set_mode((640,480))
space = pygame.Rect(0,0,0,0)
Boom = pygame.Rect(640,480,0,0)
Ship = pygame.image.load('ship.png')
Rock = pygame.image.load('Rock.png')
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
direction2 = (0,0)
rect  = False
Ship = pygame.image.load('ship.png').convert_alpha()
Ship = pygame.transform.scale(Ship, (50, 50))         
space = Ship.get_rect()
Dead = False
Rock = pygame.image.load('Rock.png').convert_alpha()
Rock = pygame.transform.scale(Rock, (50, 50))         
Boom = Rock.get_rect()
Boom.move_ip (500,400) 
  
while running:
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
              Dead = False
              rect = True
              space.topleft = (0,0)
              Boom.bottomright = (640,480)
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
           #moves the Boom Object
           #moves the object in a direction                    
            elif event.key == pygame.K_UP and rect and not Dead:
              direction2 = Up
            elif event.key == pygame.K_DOWN and rect and not Dead:      
              direction2 = Down   
            elif event.key == pygame.K_LEFT and rect and not Dead:  
              direction2 = Left
            elif event.key == pygame.K_RIGHT and rect and not Dead: 
              direction2 = Right 
                 
        #elif event.type == pygame.MOUSEMOTION:
        
            #if a mouse button event happened do this
            #get the position of the mouse
            
          #mouse_position = event.pos
           
            #change the position of the rectangle
            
          #Crash.center = mouse_position
        if event.type == pygame.KEYUP: 
          if event.key == pygame.K_w and direction == Up:   
           direction = (0,0)
          if event.key == pygame.K_a and direction == Left:
            direction = (0,0)
          if event.key == pygame.K_s and direction == Down:
            direction = (0,0)
          if event.key == pygame.K_d and direction == Right:
            direction = (0,0)
          
          if event.key == pygame.K_UP and direction2 == Up:   
           direction2 = (0,0)
          if event.key == pygame.K_LEFT and direction2 == Left:
            direction2 = (0,0)
          if event.key == pygame.K_DOWN and direction2 == Down:
            direction2 = (0,0)
          if event.key == pygame.K_RIGHT and direction2 == Right:
            direction2 = (0,0)

    if Boom.colliderect(space):
      Dead = True
    space.move_ip(direction)
    Boom.move_ip(direction2)
    window.fill((Black))
    clock.tick(30)
    if rect:
      if not Dead: window.blit(Rock,Boom)
      window.blit(Ship,space)
        #update the display
      pygame.display.update()
      Color = (130, 252, 100)
      Color2 = (0,0,100)
      
    if space.top < 0: 
     space.bottom = 480
    if space.bottom > 480: 
     space.top = 0
     
    if space.left < 0: 
      space.right = 640
    if space.right > 640: 
      space.left = 0
      
      
    if Boom.top < 0: 
     Boom.bottom = 480
    if Boom.bottom > 480: 
     Boom.top = 0
     
    if Boom.left < 0: 
      Boom.right = 640
    if Boom.right > 640: 
      Boom.left = 0
    
#this code will only run when the loop is stopped
pygame.quit()