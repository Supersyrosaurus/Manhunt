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
        #All lists are 2 dimensional, storing what needs to be displayed
        #and also the coordinates of where they should be displayed
        self.texts = []
        self.images = []
        self.buttons = []
        self.alpha = 255
        #All screens will be the same size
        self.screen = pygame.display.set_mode((960, 640))


    #Procedure to display image
    def displayImg(self):
        imageIndex = 0
        coordIndex = 0
        #Runs while both of the counters above haven't gone above the length each list within the list
        while imageIndex != len(self.images[0]) and coordIndex != len(self.images[1]):
            #Loads the image
            img = pygame.image.load(self.images[0][imageIndex]).convert_alpha()
            img.set_alpha(self.alpha)
            self.screen.blit(img, self.images[1][coordIndex])
            imageIndex += 1
            coordIndex += 1


    #Procedure to display text
    def displayText(self):
        textIndex = 0
        coordIndex = 0
        #Runs while both of the counters above haven't gone above the length each list within the list
        while textIndex != len(self.texts[0])and coordIndex != len(self.texts[1]):
            self.screen.blit(self.texts[0][textIndex], self.texts[1][coordIndex])
            textIndex += 1
            coordIndex += 1

    def createButton(self, id, image, x, y, scale):
        #Creates an object of type button with the relevant attributes
        button = Button(id, image, x, y, scale)
        #Adds the button to the list of buttons
        self.buttons.append(button)

    def searchButton(self, id):
        #Goes through each of the buttons within the list
        for button in self.buttons:
            #Compares the id of the current button to the 
            #one it is searching for
            if button.id == id:
                #returns the button object
                return button

    def closeScreen(self):
        self.alpha = 0
        self.displayImg()

    def displayScreen(self):
        pass

    def addImages(self, images, Coords):
        self.images.append(images)
        self.images.append(Coords)
        

    def addText(self, texts, Coords):
        self.texts.append(texts)
        self.texts.append(Coords)

    def setColour(self, colour):
        self.screen.fill(colour)


#Button class
class Button():
    def __init__(self, id, img, x, y, scale):
        #Identification needed for each button so that they can 
        #be differentiated and easier to find 
        self.id = id
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
    text = textFont.render(textName, True,  colour).convert_alpha()
    return text


black = (0, 0, 0)
white = (255, 255, 255)

#Screens form screen class
mainMenu = Screen()

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
    if mainMenu.searchButton('start').clickCheck() == True:
        print('Start')
    if mainMenu.searchButton('options').clickCheck() == True:
        print('Setting')


    pygame.display.update()
