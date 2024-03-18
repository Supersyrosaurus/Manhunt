import pygame
import screens
import maps
import player
import colours
import mapObjects
import hunter

#Initialising the pygame module
pygame.init()

#Setting a title
pygame.display.set_caption("Manhunt")

#Setting the icon
gameIcon = pygame.image.load('Manhunt.png')
pygame.display.set_icon(gameIcon)

#Setting FPS
clock = pygame.time.Clock()



#Screens form screen class
mainMenu = screens.Screen(colours.lightGrey)
settings = screens.Screen(colours.lightGrey)
mode = screens.Screen(colours.lightGrey)
game = screens.GameScreen(colours.lightGrey)
win = screens.Screen(colours.lightGrey)

#Variables for mainMenu
mainMenu_texts = ['Manhunt']
mainMenu_textSizes = [160]
mainMenu_textColours = [colours.black]
mainMenu_textFonts = [None]
mainMenu_textCoords = [(230, 80)]
mainMenu_images = []
mainMenu_imagesCoords = []
mainMenu_imagescales = []
mainMenu.renderMTexts(mainMenu_texts, mainMenu_textSizes, mainMenu_textColours, mainMenu_textFonts, mainMenu_textCoords)
mainMenu.createButton('start','Start.png', 340, 175, 1)
mainMenu.createButton('options', 'settings.png', 5, 585, 0.1)
mainMenu.addImages(mainMenu_images, mainMenu_imagesCoords, mainMenu_imagescales)

#Variables for settings class
settings_texts = ['Settings', 'W: Move Forward', 'A: Move Left', 'S: Move Backward', 'D: Move Right', 'Shift: Sprint', 'E: Interact' ]
settings_textSizes = [160, 50, 50, 50, 50, 50, 50]
settings_textColours = [colours.black, colours.black, colours.black, colours.black, colours.black, colours.black, colours.black]
settings_textFonts = [None, None, None, None, None, None, None]
settings_textCoords = [(230, 80), (300,250), (300,310), (300,370), (300,430), (300,490), (300, 550)]
settings_images = []
settings_imagesCoords = []
settings_imageScales = []
settings.renderMTexts(settings_texts, settings_textSizes, settings_textColours, settings_textFonts, settings_textCoords)
settings.createButton('return','return.png', 10, 10, 0.1)
settings.addImages(settings_images, settings_imagesCoords, settings_imageScales)

#Variables for GameScreen class
game_texts = []
game_textSizes = []
game_textColours = []
game_textFonts = []
game_textCoords = []
game_images = []
game_imageCoords = []
game_imageScales = []
game.renderMTexts(game_texts, game_textSizes, game_textColours, game_textFonts, game_textCoords)
game.addImages(game_images, game_imageCoords, game_imageScales)


def mainMenuScreen(mainMenu, settings, clock):
    running = True
    while running:
        clock.tick(60)
        mainMenu.displayScreen()
        if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
            running = gameScreen(clock)
            print('Start')
        if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
            running = settingsScreen(settings, clock)
            print('settings')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

def settingsScreen(settings, clock):
    running = True
    while running:
        clock.tick(60)
        settings.displayScreen()
        if settings.searchButton('return').clickCheck(settings.screen) == True:
            return True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()



#Creating the map for the game
walls = {'empty':mapObjects.empty, 'hidingSpace':mapObjects.hidingSpace, 'lever':mapObjects.lever}
floors = {'wood':mapObjects.wood, 'concrete':mapObjects.concrete, 'carpet':mapObjects.carpet}
doorCoord = mapObjects.doors
map = maps.Map(walls, floors, doorCoord, 20, 30)
map.createMap()
mapList = map.getMap()

playerX = 3
playerY = 6
playerOne = player.Player(playerX * 32, playerY * 32, 'BlueCircle.png', 1, 2, 2, map)
playerOne.setMaxLevers(map)

hunterX = 15
hunterY = 10
hunterOne = hunter.Hunter(hunterX * 32, hunterY * 32, 'RedCircle.png', 1, 2, 2)

def gameScreen(clock):
        running = True
        done = 0
        while running:
            clock.tick(120)
            game.displayGameScreen(map.getMap())
            playerWin = playerOne.ready(map, game, hunterOne)
            hunterWin = hunterOne.ready(game.getScreen(), map, playerOne)
            if playerWin:
                return False
                running = winScreen(clock)
            if hunterWin:
                return False
                running = winScreen(clock)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                playerOne.interactCheck(event, map)

            pygame.display.update()




mainMenuScreen(mainMenu, settings, clock)

