import pygame
import classes

#Initialising the pygame module
pygame.init()

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
mode = classes.Screen()

#Variables for mainMenu
mainMenu_texts = ['Manhunt']
mainMenu_textSizes = [160]
mainMenu_textColours = [black]
mainMenu_textFonts = [None]
mainMenu_textCoords = [(230, 80)]
mainMenu_images = ['Manhunt.png']
mainMenu_imagesCoords = [(32, 32)]
mainMenu_imagescales = [1]
mainMenu.renderMTexts(mainMenu_texts, mainMenu_textSizes, mainMenu_textColours, mainMenu_textFonts, mainMenu_textCoords)
mainMenu.createButton('start','Start.png', 340, 175, 1)
mainMenu.createButton('options', 'settings.png', 5, 585, 0.1)
mainMenu.addImages(mainMenu_images, mainMenu_imagesCoords, mainMenu_imagescales)
mainMenu.setColour((150, 150, 150))

#Variables for settings class
settings_texts = ['Settings']
settings_textSizes = [160]
settings_textColours = [black]
settings_textFonts = [None]
settings_textCoords = [(230, 80)]
settings_images = []
settings_imagesCoords = []
settings_imageScales = []
settings.renderMTexts(settings_texts, settings_textSizes, settings_textColours, settings_textFonts, settings_textCoords)
settings.createButton('return','return.png', 10, 10, 0.1)
'''settings.createButton('options', 'settings.png', 5, 585, 0.1)'''
settings.addImages(settings_images, settings_imagesCoords, settings_imageScales)
settings.setColour((200, 200, 200))

#Variables for mode class
mode_texts = ['Mode']
mode_textSizes = [160]
mode_textColours = [black]
mode_textFonts = [None]
mode_textCoords = [(230, 80)]
mode_images = []
mode_imagesCoords = []
mode_imageScales = []
settings.renderMTexts(mode_texts, mode_textSizes, mode_textColours, mode_textFonts, mode_textCoords)
#mode.createButton('normal', )

def mainMenuScreen(mainMenu, settings):
    running = True
    while running:
        mainMenu.displayScreen()
        if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
            #running = modeScreen(mode)
            print('Start')
        if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
            running = settingsScreen(settings)
            print('settings')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

def modeScreen(mode):
    running = True
    while running:
        mode.displayScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

def settingsScreen(settings):
    running = True
    while running:
        settings.displayScreen()
        if settings.searchButton('return').clickCheck(settings.screen) == True:
            return True
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




