import pygame
import classes

#Initialising the pygame module
pygame.init()

'''#Creating a screen
screenHeight = 640
screenWidth = 960
screen = pygame.display.set_mode((screenWidth, screenHeight))'''


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

#Variables for mainMenu
mainMenu_texts = ['Manhunt', 'SUI']
mainMenu_textSizes = [160, 130]
mainMenu_textColours = [black, white]
mainMenu_textFonts = [None, None]
mainMenu_textCoords = [(230, 80), (230, 240)]
mainMenu_images = ['Manhunt.png', 'start.png' ]
mainMenu_imagesCoords = [(32, 32), (400, 400)]
mainMenu_imagescales = [1, 1]
mainMenu.renderMTexts(mainMenu_texts, mainMenu_textSizes, mainMenu_textColours, mainMenu_textFonts, mainMenu_textCoords)
mainMenu.createButton('start','rectangleStart.png', 250, 150, 0.8)
mainMenu.createButton('options', 'settings.png', 5, 585, 0.1)
mainMenu.addImages(mainMenu_images, mainMenu_imagesCoords, mainMenu_imagescales)
mainMenu.setColour((150, 150, 150))

#Variables for settings class
settings_texts = ['Settings', 'SUI']
settings_textSizes = [160, 130]
settings_textColours = [black, white]
settings_textFonts = [None, None]
settings_textCoords = [(230, 80), (230, 500)]
settings_images = ['Manhunt.png', 'start.png' ]
settings_imagesCoords = [(32, 32), (400, 400)]
settings_imageScales = [1, 1]
settings.renderMTexts(settings_texts, settings_textSizes, settings_textColours, settings_textFonts, settings_textCoords)
settings.createButton('start','rectangleStart.png', 250, 150, 0.8)
settings.createButton('options', 'settings.png', 5, 585, 0.1)
settings.addImages(mainMenu_images, mainMenu_imagesCoords, settings_imageScales)
settings.setColour((150, 150, 150))




def mainMenuScreen(mainMenu, settings):
    running = True
    while running:
        mainMenu.displayScreen()
        if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
            print('Start')
        if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
            running = settingsScreen(settings)
            print('settings')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

def settingsScreen(settings):
    running = True
    while running:
        settings.displayScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()



mainMenuScreen(mainMenu, settings)


#Loop for game screen
'''running = True'''
'''while running:

    #Changing background colour
    mainMenu.displayScreen()
    if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
        print('Start')
    if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
        mainMenu.closeScreen()
        settings.displayScreen()
        print('Setting')


    #event handler
    for event in pygame.event.get():
        #Checks through all of the events that are happening in the window
        #If user presses cross button window closed
        if event.type == pygame.QUIT:
            running = False'''
        
'''        if settings.searchButton('start').clickCheck(mainMenu.screen) == True:
            print('Start')
        if settings.searchButton('options').clickCheck(mainMenu.screen) == True:
            settings()
            print('settings')
            running = False'''




