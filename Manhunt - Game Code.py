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

print(str(gameIcon.get_rect()))
print(str(gameIcon.get_width()))
print(str(gameIcon.get_height()))

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


    def clickCheck(self):
        pos = pygame.mouse.get_pos()
        #print(pos)
        #Is mouse cursor colliding with the rectangle of image
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                print('LESS GOO')


    def draw(self):
        #draws image on the screen
        screen.blit(self.transformedImg, (self.rect.x, self.rect.y))
        self.clickCheck()
    


#Procedure to display image
def displayImg(imgName, x, y):
    #Loads the image
    img = pygame.image.load(imgName)
    screen.blit(img, (x, y))

#Procedure to display text
def displayText(textName, x, y, size, colour = (0,0,0), font = None):
    #Sets font(I/A) and size of the text
    textFont = pygame.font.Font(font, size)
    #Renders the text with anti aliasing(Boolean) and colour (Tuple) 
    text = textFont.render(textName, True,  colour)
    screen.blit(text, (x, y))

startButton = Button('rectangleStart.png', 250, 150, 0.8)

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
    displayText('Manhunt', 230, 80, 160)
    displayImg('Manhunt.png', 32, 32)
    startButton.draw()
    pygame.display.update()
