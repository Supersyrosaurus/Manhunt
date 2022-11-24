import pygame

#Initialising the pygame module
pygame.init()

#Creating a screen
screenHeight = 640
screenWidth = 960
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Setting a title
pygame.display.set_caption("Manhunt")

#Setting the icon
gameIcon = pygame.image.load('Manhunt.png')
pygame.display.set_icon(gameIcon)

#Loading the start button
startImg = pygame.image.load('rectangleStart.png')

#Displaying text
manhuntNameFont = pygame.font.Font("VINERITC.TTF", 200)
manhuntName = manhuntNameFont.render('Manhunt', True, (0,0,0))

#Loop for game screen
running = True
while running:
    #event handler
    for event in pygame.event.get():
        #Checks through all of the events that are happening in the window
        #If user presses cross button window closed
        if event.type == pygame.QUIT:
            running = False
    
    #Changing background colour
    screen.fill((75,75,75))
    screen.blit(manhuntName,(225, 80))
    screen.blit(gameIcon, (445, 130) )
    screen.blit(startImg, (350, 160))
    pygame.display.update()
