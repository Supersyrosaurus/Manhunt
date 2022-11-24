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
'''startImg = pygame.image.load('rectangleStart.png')'''

#Displaying text
'''manhuntNameFont = pygame.font.Font(None, 160)
manhuntName = manhuntNameFont.render('Manhunt', True, (0,0,0))'''

#Procedure to display image
def displayImg(imgName, x, y):
    img = pygame.image.load(imgName)
    screen.blit(img, (x, y))

#Procedure to display text
def displayText(textName, x, y, size, colour = (0,0,0), font = None):
    textFont = pygame.font.Font(font, size)
    text = textFont.render(textName, True,  colour)
    screen.blit(text, (x, y))



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
    displayText('Manhunt', 230, 80, 160)
    displayImg('Manhunt.png', 32, 32)
    displayImg('rectangleStart.png', 350, 160)
    pygame.display.update()
