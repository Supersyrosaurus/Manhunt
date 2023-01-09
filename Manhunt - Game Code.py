import pygame
import screens
import objects
import maps
import physics

#Initialising the pygame module
pygame.init()

#Setting a title
pygame.display.set_caption("Manhunt")

#Setting the icon
gameIcon = pygame.image.load('Manhunt.png')
pygame.display.set_icon(gameIcon)

#Setting FPS
clock = pygame.time.Clock()

black = (0, 0, 0)
red = (155, 0, 0)
white = (255, 255, 255)
lightGrey = (150,150,150)

#Screens form screen class
mainMenu = screens.Screen(lightGrey)
settings = screens.Screen(lightGrey)
mode = screens.Screen(lightGrey)
game = screens.GameScreen(lightGrey)

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

'''#Creating the map for the game
walls = {'empty':[(1,1)], 'hidingSpace':[(2,2)], 'lever':[(3,2)]}
floors = {'wood':[(1,4),(5,4)], 'concrete':[(1,5),(2,5),], 'carpet':[(4,3)]}
doorCoord = (3 ,6)
map = maps.Map(walls, floors, doorCoord, 20)
map.createMap()
mapList = map.getMap()
print(mapList)'''

def mainMenuScreen(mainMenu, settings, mode, clock):
    running = True
    while running:
        clock.tick(60)
        mainMenu.displayScreen()
        if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
            running = modeScreen(mode, clock)
            print('Start')
        if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
            running = settingsScreen(settings, clock)
            print('settings')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

def modeScreen(mode, clock):
    running = True
    while running:
        clock.tick(60)
        mode.displayScreen()
        if mode.searchButton('return').clickCheck(mode.screen) == True:
            return True
        if mode.searchButton('normal').clickCheck(mode.screen) == True:
            print('normal')
            running = gameScreen(clock)
        if mode.searchButton('nightmare').clickCheck(mode.screen) == True:
            print('NIGHTMARE')
            running = gameScreen(clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
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

#Testing rectangles collisions
movingRect = pygame.Rect(25, 50, 80, 80)
otherRect =pygame.Rect(150, 300, 400, 100)

def setSpeed(rect, screen):
        global xSpeed, ySpeed, otherSpeed
        rect.x += xSpeed
        rect.y += ySpeed
        
        #Collsion with screen borders
        if rect.right >= screen.getWidth() or rect.left <= 0:
            xSpeed *= -1
            print(xSpeed)
        if rect.top <= 0 or rect.bottom >= screen.getHeight():
            ySpeed *= -1
            print(xSpeed)

        #Moving other rect
        otherRect.y += otherSpeed
        if otherRect.top <= 0 or otherRect.bottom >= screen.getHeight():
            otherSpeed *= -1 

        #Collision with other rects
        collisionTolerance = 10
        if movingRect.colliderect(otherRect):
            if abs(otherRect.top - movingRect.bottom) < collisionTolerance and ySpeed > 0:
                ySpeed *= -1
            if abs(otherRect.bottom - movingRect.top) < collisionTolerance and ySpeed < 0:
                ySpeed *= -1
            if abs(otherRect.right - movingRect.left) < collisionTolerance and xSpeed > 0:
                xSpeed *= -1
            if abs(otherRect.left - movingRect.right) < collisionTolerance and xSpeed < 0:
                xSpeed *= -1
            

        pygame.draw.rect(screen.getScreen(), (0,0,0), rect)

xSpeed = 4
ySpeed = 2
otherSpeed = 2

def gameScreen(clock):
        running = True
        while running:
            clock.tick(60)
            game.displayScreen()
            setSpeed(movingRect, game)
            pygame.draw.rect(game.getScreen(), (255, 0, 255), otherRect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
            pygame.display.update()

mainMenuScreen(mainMenu, settings, mode, clock)

'''#Wall testing stuff 
#Initialising the pygame module
pygame.init()

wallsDic = {'empty':[(1,1)], 'hidingSpace':[(2,2)], 'lever':[(3,2)]}
floorsDic = {'wood':[(1,4),(5,4)], 'concrete':[(1,5),(2,5),], 'carpet':[(4,3)]}
doorCoord = (3 ,6)

gameMap = maps.Map(wallsDic, floorsDic, doorCoord, 5)
gameMap.createMap()
for y in gameMap.map:
    print(y)
print(gameMap.getFloors('wood'))
print(gameMap.getObject((3,6)))
print(gameMap.getWalls())'''


#Loop for game screen
'''running = True
while running:

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

#Going through a dictionary
'''print(wallsDic)
for list in wallsDic:
    print(wallsDic[list])
    for element in wallsDic[list]:
        print(element)'''


