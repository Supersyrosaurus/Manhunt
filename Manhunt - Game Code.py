import pygame
import classes

#Initialising the pygame module
pygame.init()

#Creating a screen
'''screenHeight = 640
screenWidth = 960
screen = pygame.display.set_mode((screenWidth, screenHeight))'''

#Setting a title
pygame.display.set_caption("Manhunt")

#Setting the icon
gameIcon = pygame.image.load('Manhunt.png')
pygame.display.set_icon(gameIcon)


def renderText(textName, size, colour = (0,0,0), font = None):
    #Sets font(I/A) and size of the text
    textFont = pygame.font.Font(font, size)
    #Renders the text with anti aliasing(Boolean) and colour (Tuple) 
    text = textFont.render(textName, True,  colour).convert_alpha()
    return text


black = (0, 0, 0)
white = (255, 255, 255)

#Screens form screen class
mainMenu = classes.Screen()

#Variables
mainMenu_text = [renderText('Manhunt', 160)]
mainMenu_textCoords = [(230, 80), (230, 240)]
mainMenu_images = ['Manhunt.png', 'start.png' ]
mainMenu_imagesCoords = [(32, 32), (400, 400)]
mainMenu.createButton('start','rectangleStart.png', 250, 150, 0.8)
mainMenu.createButton('options', 'settings.png', 5, 585, 0.1)
mainMenu.addText(mainMenu_text, mainMenu_textCoords)
mainMenu.addImages(mainMenu_images, mainMenu_imagesCoords)


mainMenu.setColour((150, 150, 150))

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
    mainMenu.displayText()
    mainMenu.displayImg()
    if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
        print('Start')
    if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
        print('Setting')


    pygame.display.update()
