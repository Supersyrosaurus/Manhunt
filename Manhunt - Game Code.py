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
red = (155, 0, 0)
white = (255, 255, 255)
lightGrey = (150,150,150)

#Screens form screen class
mainMenu = classes.Screen(lightGrey)
settings = classes.Screen(lightGrey)
mode = classes.Screen(lightGrey)

#Variables for mainMenu
mainMenu_texts = ['Manhunt']
mainMenu_textSizes = [160]
mainMenu_textColours = [black]
mainMenu_textFonts = [None]
mainMenu_textCoords = [(230, 80)]
mainMenu_images = []
mainMenu_imagesCoords = []
mainMenu_imagescales = []
mainMenu.renderMTexts(mainMenu_texts, mainMenu_textSizes, mainMenu_textColours, mainMenu_textFonts, mainMenu_textCoords)
mainMenu.createButton('start','Start.png', 340, 175, 1)
mainMenu.createButton('options', 'settings.png', 5, 585, 0.1)
mainMenu.addImages(mainMenu_images, mainMenu_imagesCoords, mainMenu_imagescales)
#mainMenu.setColour((150, 150, 150))

#Variables for settings class
settings_texts = ['Settings', 'W: Move Forward', 'A: Move Left', 'S: Move Backward', 'D: Move Right', 'Shift: Sprint', 'E: Interact' ]
settings_textSizes = [160, 50, 50, 50, 50, 50, 50]
settings_textColours = [black, black, black, black, black, black, black]
settings_textFonts = [None, None, None, None, None, None, None]
settings_textCoords = [(230, 80), (300,250), (300,310), (300,370), (300,430), (300,490), (300, 550)]
settings_images = []
settings_imagesCoords = []
settings_imageScales = []
settings.renderMTexts(settings_texts, settings_textSizes, settings_textColours, settings_textFonts, settings_textCoords)
settings.createButton('return','return.png', 10, 10, 0.1)
settings.addImages(settings_images, settings_imagesCoords, settings_imageScales)
#settings.setColour((200, 200, 200))

#Variables for mode class
mode_texts = ['Mode']
mode_textSizes = [160]
mode_textColours = [black]
mode_textFonts = [None]
mode_textCoords = [(320, 80)]
mode_images = []
mode_imagesCoords = []
mode_imageScales = []
mode.renderMTexts(mode_texts, mode_textSizes, mode_textColours, mode_textFonts, mode_textCoords)
mode.createButton('return','return.png', 10, 10, 0.1)
mode.createButton('normal', 'normal.png', 340, 175, 1)
mode.createButton('nightmare', 'nightmare.png', 283, 375, 1)
mode.addImages(mode_images, mode_imagesCoords, mode_imageScales)

def mainMenuScreen(mainMenu, settings, mode):
    running = True
    while running:
        mainMenu.displayScreen()
        if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
            running = modeScreen(mode)
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
        if mode.searchButton('return').clickCheck(mode.screen) == True:
            return True
        if mode.searchButton('normal').clickCheck(mode.screen) == True:
            print('normal')
        if mode.searchButton('nightmare').clickCheck(mode.screen) == True:
            print('NIGHTMARE')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        pygame.display.update()

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



mainMenuScreen(mainMenu, settings, mode)


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




