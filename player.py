import pygame
import maps
import objects
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img, scale, xSpeed, ySpeed):
        super().__init__
        self.x = x
        self.y = y
        self.screenCoords = (x, y)
        self.mapCoords = (x/32, y/32)
        self.img = pygame.image.load(img).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height()
        self.transformedImg = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.hitbox = self.transformedImg.get_rect()
        self.hiding = False

    #Displays the player on whatever screen is passed to the method
    def displayPlayer(self, screen):
        screen.blit(self.transformedImg, self.screenCoords)

    #Checks if the W key has been pressed and if it has then it deducts 1 from the player coordinates and update
    #the coordinates of the player
    def moveForward(self, pressed):
        if pressed[pygame.K_w]:
            self.y -= self.ySpeed
            self.setCoords()
            #print('forward')
            

    #Checks if the S key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def moveBackward(self, pressed):
        if pressed[pygame.K_s]:
            self.y += self.ySpeed
            self.setCoords()
            #print('backward')

    #Checks if the D key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def moveRight(self, pressed):
        if pressed[pygame.K_d]:
            self.x += self.xSpeed
            self.setCoords()
            #print('right')
        

    #Checks if the A key has been pressed and if it has then it deducts 1 from the players coordinates and updates 
    #the coordintes of the player
    def moveLeft(self, pressed):
        if pressed[pygame.K_a]:
            self.x -= self.xSpeed
            self.setCoords()
            #print('left')

    def interact(self, pressed, map):
        if pressed[pygame.K_e]:
            coords = self.getMapCoords()
            hidingSpace = map.getObject(coords)
            print(hidingSpace)
            if isinstance(hidingSpace, objects.HidingSpace):
                print('THIS IS A HIDING SPACE')
            

            print('interact')

    def sprint(self, pressed):
        if pressed[pygame.K_LSHIFT]:
            print('sprint')

    #This changes the coordinates of the player whenever it is called, as the map coordinates of the player are directly linked to the 
    #screen coordinates of the player, by changing the screen coordinates (which moves the player image and rect) it also changes the
    #players location on the other map
    def setCoords(self):
        self.screenCoords = (self.x, self.y)
        #print(str(self.screenCoords))
    
    def setMapCoords(self):
        x = round(int(self.screenCoords[0])/32)
        y = round(int(self.screenCoords[1])/32)
        self.mapCoords = (x, y)

    #This method checks if the W, A, S, D, E, or LEFT SHIFT buttons are pressed and then carries out various actions depending 
    #on the button that is pressed 
    def checkKeys(self, map):
        #Uses a pygame method to check if any key has been pressed and will be true if it is pressed and false if no buttons
        #on the keyboard are being pressed
        pressed = pygame.key.get_pressed()

        #Each of these methods control an aspect of the inputs from the user which in turn controls the player
        self.moveForward(pressed)
        self.moveBackward(pressed)
        self.moveRight(pressed)
        self.moveLeft(pressed)
        self.sprint(pressed)
        self.interact(pressed, map)

    #Returns the map coordinates of the player
    def getMapCoords(self):
        self.setMapCoords()
        return self.mapCoords





 

        