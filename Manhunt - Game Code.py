import pygame

#Initialising the pygame module
pygame.init()

#Creating a screen
screen = pygame.display.set_mode((1440,810))

#Setting a title
pygame.display.set_caption("Manhunt")

#Setting the icon
gameIcon = pygame.image.load('Manhunt.png')
pygame.display.set_icon(gameIcon)

#Loop for game screen
running = True
while running:
    for event in pygame.event.get():
        #Checks through all of the events that are happening in the window
        #If the event is the user pressing the quit button(pygame.QUIT) then the window is closed
        if event.type == pygame.QUIT:
            running = False
    
    #Changing background colour
    screen.fill((75,75,75))
    pygame.display.update()
