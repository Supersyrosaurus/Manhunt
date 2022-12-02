import pygame
import classes

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


black = (0, 0, 0)
white = (255, 255, 255)

#Screens form screen class
mainMenu = classes.Screen()
settings = classes.Screen()

#Variables
mainMenu_texts = ['Manhunt', 'SUI']
mainMenu_textSizes = [160, 130]
mainMenu_textColours = [black, white]
mainMenu_textFonts = [None, None]
mainMenu_textCoords = [(230, 80), (230, 240)]
mainMenu_images = ['Manhunt.png', 'start.png' ]
mainMenu_imagesCoords = [(32, 32), (400, 400)]
mainMenu.renderMTexts(mainMenu_texts, mainMenu_textSizes, mainMenu_textColours, mainMenu_textFonts, mainMenu_textCoords)
mainMenu.createButton('start','rectangleStart.png', 250, 150, 0.8)
mainMenu.createButton('options', 'settings.png', 5, 585, 0.1)
mainMenu.addImages(mainMenu_images, mainMenu_imagesCoords)


mainMenu.setColour((150, 150, 150))

#Loop for game screen
running = True
while running:

    #Changing background colour
    mainMenu.displayScreen()
    if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
        print('Start')
    if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
        #settings.displayScreen()
        print('Setting')


    #event handler
    for event in pygame.event.get():
        #Checks through all of the events that are happening in the window
        #If user presses cross button window closed
        if event.type == pygame.QUIT:
            running = False
    



    pygame.display.update()
