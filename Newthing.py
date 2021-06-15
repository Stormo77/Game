import pygame

pygame.init()
#the code for your game has to go between these two lines

#create a window object
window = pygame.display.set_mode((640,480))
#create a game loop
running = True #game state
#color the window background
Black = (0,0,0)
window.fill((Black))
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
#this code will only run when the loop is stopped
pygame.quit()