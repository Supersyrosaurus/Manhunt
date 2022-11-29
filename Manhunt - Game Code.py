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


#Screen class
class Screen():
    def __init__(self):
        self.texts = []
        self.images = []
        self.buttons = []
        self.screen = pygame.display.set_mode((960, 640))

    #Procedure to display image
    def displayImg(self, imgName, x, y):
        #Loads the image
        img = pygame.image.load(imgName)
        self.screen.blit(img, (x, y))

    #Procedure to display text
    def displayText(self):
        textIndex = 0
        coordIndex = 0
        while textIndex != len(self.texts[0])and coordIndex != len(self.texts[1]):
            self.screen.blit(self.texts[0][textIndex], self.texts[1][coordIndex])
            textIndex = textIndex + 1
            coordIndex = coordIndex + 1

    def closeScreen(self):
        pass

    def displayScreen(self):
        pass

    def addImages(self, images, Coords):
        self.images.append(images)
        self.images.append(Coords)

    def addButtons(self, buttons):
        self.buttons.append(buttons)

    def addText(self, texts, Coords):
        self.texts.append(texts)
        self.texts.append(Coords)

        


#Button class
class Button():
    def __init__(self, img, x, y, scale):
        #Loads the image 
        self.img = pygame.image.load(img).convert_alpha()
        #Gets the width and height of the img in pixels 
        width = self.img.get_width()
        height = self.img.get_height()
        print(width)
        print(height)
        #Transforms the image using a scale
        self.transformedImg = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))
        #Gets the rectangular area of the image
        self.rect = self.transformedImg.get_rect()
        #Is the top left of the image
        self.rect.topleft = (x, y)
        self.clicked = False


    def draw(self):
        #draws image on the screen
        screen.blit(self.transformedImg, (self.rect.x, self.rect.y))

    def clickCheck(self):
        self.draw()
        hasClicked = False
        pos = pygame.mouse.get_pos()
        #print(pos)
        #Is mouse cursor colliding with the rectangle of image
        if self.rect.collidepoint(pos):
            #Checks if the mouse has been pressed and has already been pressed before
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                #Set to true so that button is only registered once with one mouse click
                self.clicked = True
                hasClicked = True
        #If the user is not pressing the mouse button it is reset so that the user
        #can use it again
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        #Returns whether the mouse has been clicked or not
        return hasClicked
                

def renderText(textName, size, colour = (0,0,0), font = None):
    #Sets font(I/A) and size of the text
    textFont = pygame.font.Font(font, size)
    #Renders the text with anti aliasing(Boolean) and colour (Tuple) 
    text = textFont.render(textName, True,  colour)
    return text


#Screens form screen class
mainMenu = Screen()

#Variables
startButton = Button('rectangleStart.png', 250, 150, 0.8)

#Lists
mainMenu_text = [renderText('Manhunt', 160)]
mainMenu_textCoords = [(230, 80)]
mainMenu_images = []
mainMenu_imagesX = []
mainMenu_imagesY = []


mainMenu.addText(mainMenu_text, mainMenu_textCoords)
mainMenu_buttons = [startButton]

doesWork = renderText('Manhunt', 160)

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
    mainMenu.displayText()
    '''mainMenu.displayText(doesWork, 230, 80)'''
    '''    displayText('Manhunt', 230, 80, 160)
    displayImg('Manhunt.png', 32, 32)'''
    if startButton.clickCheck() == True:
        print('Start')

    pygame.display.update()
