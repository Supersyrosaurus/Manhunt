import pygame

pygame.init()


#Screen class
class Screen():
    def __init__(self, colour):
        self.colour = colour
        #All lists are 2 dimensional, storing what needs to be displayed
        #and also the coordinates of where they should be displayed
        self.texts = []
        self.images = []
        self.buttons = []
        #All screens will be the same size
        self.screen = pygame.display.set_mode((960, 640))


    #Procedure to display image
    def displayImg(self):
        imageIndex = 0
        #Runs while both of the counters above haven't gone above the length each list within the list
        while imageIndex != len(self.images[0]):
            #Loads the image
            img = pygame.image.load(self.images[0][imageIndex]).convert_alpha()
            width = img.get_width()
            height = img.get_height()
            scaleImg = pygame.transform.scale(img, (int(width * self.images[2][imageIndex]), int(height * self.images[2][imageIndex])))
            self.screen.blit(scaleImg, self.images[1][imageIndex])
            imageIndex += 1

    #Procedure to render multiple lines of text
    def renderMTexts(self, texts, sizes, colours, fonts, textCoords):
        textList = []
        counter = 0
        #Goes though each string of text in the list
        while counter != len(texts):
            #Uses the renderText method to render the text
            render = self.renderText(texts[counter], sizes[counter], colours[counter], fonts[counter])
            #Appends each render of texts to the textList for later
            textList.append(render)
            counter += 1
            #Both the list of rendered texts and the list of coordinates are
            #appended to the texts list within the class
        self.texts.append(textList)
        self.texts.append(textCoords)

    #Function to render text
    def renderText(self, textName, size, colour, font):
        #Sets font(I/A) and size of the text
        textFont = pygame.font.Font(font, size)
        #Renders the text with anti aliasing(Boolean) and colour (Tuple) 
        text = textFont.render(textName, True,  colour).convert_alpha()
        return text


    #Procedure to display text
    def displayText(self):
        textIndex = 0
        #Runs while both of the counters above haven't gone above the length each list within the list
        while textIndex != len(self.texts[0]):
            self.screen.blit(self.texts[0][textIndex], self.texts[1][textIndex])
            textIndex += 1

    #Procedure which accesses the Button class to create a button and then attributes it to this specific class
    def createButton(self, id, image, x, y, scale):
        #Creates an object of type button with the relevant attributes
        button = Button(id, image, x, y, scale)
        #Adds the button to the list of buttons
        self.buttons.append(button)

    #Function which searches and returns a button based on the ID of the button
    def searchButton(self, id):
        #Goes through each of the buttons within the list
        for button in self.buttons:
            #Compares the id of the current button to the 
            #one it is searching for
            if button.id == id:
                #returns the button object
                return button

    #Procedure which displays a new screen 
    def displayScreen(self):
        #Colours the screen and covers all blitted things
        self.screen.fill(self.colour)
        self.displayImg()
        self.displayText()

    #Procedure which appends all image based things into the images list
    def addImages(self, images, Coords, scale):
        self.images.append(images)
        self.images.append(Coords)
        self.images.append(scale)
        
    #Procedure which sets colour of the screen
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

    def draw(self, screen):
        #draws image on the screen
        screen.blit(self.transformedImg, (self.rect.x, self.rect.y))

    def clickCheck(self, screen):
        self.draw(screen)
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
                
