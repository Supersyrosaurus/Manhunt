import pygame
import screens
import objects
import maps
import physics
import player
import colours
import mapObjects

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
#settings.setColour((200, 200, 200))

#Variables for mode class
mode_texts = ['Mode']
mode_textSizes = [160]
mode_textColours = [colours.black]
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
        global otherSpeed, xSpeed, ySpeed
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
        #Checking if the moving rectangle has collided with another rectangle
        if movingRect.colliderect(otherRect):
            #Each one of these checks in what way the rectangles have collided with each other
            #As the 'movingRect' must go in the opposite direction when it hits a different object, to know which 
            #direction to move it in, we need to check how one rectangle has collided relative to the other
            #to do this we compare the absolute values of the difference of the opposite sides of each of the rectangles
            #to the collisionTollerance (which is how close one rect must be to the other in pixels to be considered a collision)
            #and we also need to check in which direction the object is moving by comparing the speed of the object in a specific direction
            #as one of the objects may have collided with another object and they are moving in the same direction which could cause the object
            #to move in the opposite direction even though it should still continue in the same direction 
            if abs(otherRect.top - movingRect.bottom) < collisionTolerance and ySpeed > 0:
                ySpeed *= -1
                print(ySpeed)
            if abs(otherRect.bottom - movingRect.top) < collisionTolerance and ySpeed < 0:
                ySpeed *= -1
                print(ySpeed)
            if abs(otherRect.left - movingRect.right) < collisionTolerance and xSpeed > 0:
                xSpeed *= -1
                print(xSpeed)
            if abs(otherRect.right - movingRect.left) < collisionTolerance and xSpeed < 0:
                xSpeed *= -1
                print(xSpeed)
            
        #This redraws the 'movingRect' - 'otherRect' is drawn in main game loop
        pygame.draw.rect(screen.getScreen(), (0,0,0), rect)

xSpeed = 3
ySpeed = 3
otherSpeed = 2
#projectile1 = physics.Projectile((100,100), 3, 3, 50, 50)
#projectile2 = physics.Projectile((500,500), -5, -5, 50, 50)


########## TESTING DA MAP STOOF ##########

#Creating the map for the game
walls = {'empty':mapObjects.empty, 'hidingSpace':mapObjects.hidingSpace, 'lever':mapObjects.lever}
floors = {'wood':mapObjects.wood, 'concrete':mapObjects.concrete, 'carpet':mapObjects.carpet}
doorCoord = mapObjects.doors
map = maps.Map(walls, floors, doorCoord, 20, 30)
map.createMap()
mapList = map.getMap()
print(mapList)

playerX = 3
playerY = 6
playerOne = player.Player(playerX * 32, playerY * 32, 'whiteCircle.png', 1, 2, 4, map)
playerOne.setMaxLevers(map)


def gameScreen(clock):
        running = True
        while running:
            clock.tick(60)
            game.displayGameScreen(map.getMap(), game.getScreen())
            playerOne.displayPlayer(game.getScreen())
            playerOne.fov(map, game)
            playerOne.checkCollision(map)

            
            canPress = True 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if canPress == True:
                    playerOne.checkKeys(map)
                    canPress = False
                
                'print(playerOne.forward, playerOne.backward, playerOne.left, playerOne.right)'
                
            pygame.display.update()

mainMenuScreen(mainMenu, settings, mode, clock)


#####################          STUFF THAT MAY BE NEEDED LATER OR HAS BEEN USED FOR TESTING          ###################

'''setSpeed(movingRect, game)
            pygame.draw.rect(game.getScreen(), (255, 0, 255), otherRect)
            projectile1.launchProjectile(game)
            projectile2.launchProjectile(game)
            canPress = True
                pressed = pygame.key.get_pressed()
                
                if pressed[pygame.K_w] and canPress == True:
                    projectile1.xCollide()
                    print(str(projectile1.xSpeed))
                    canPress = False
                    
                if pressed[pygame.K_s] and canPress == True:
                    projectile1.yCollide()
                    print(str(projectile1.ySpeed))
                    canPress = False'''







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


