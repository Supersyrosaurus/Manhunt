import pygame
import maps
import objects
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img, scale, speed):
        super().__init__
        #Coordinate attributes
        self.x = x
        self.y = y
        #self.screenCoords = (x, y)
        #self.mapCoords = (x/32, y/32)
        #Image attributes
        self.img = pygame.image.load(img).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height()
        self.transformedImg = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))
        self.width = self.transformedImg.get_width()
        self.height = self.transformedImg.get_height()
        #Hitbox of the player by creating a rectangle around the player img
        self.hitbox = self.transformedImg.get_rect()
        #Activation area for the player to use to detect levers and hiding places around the player when the player interacts
        self.activationArea = pygame.Rect(self.x - 32, self.y - 32, self.width * 3, self.height * 3)
        #Speed in any direction
        self.speed = speed
        #This is the sprinting multiplier which increases the speed of the player by that much
        self.sprint = 3
        self.hiding = False

    #Displays the player on whatever screen is passed to the method
    def displayPlayer(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.activationArea)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox)
        screen.blit(self.transformedImg, self.hitbox.topleft)
        

    #Checks if the W key has been pressed and if it has then it deducts 1 from the player coordinates and update
    #the coordinates of the player
    def moveForward(self, pressed, sprintCheck):
        if pressed[pygame.K_w] and sprintCheck:
            self.y -= self.speed * self.sprint
        if pressed[pygame.K_w]:
            self.y -= self.speed
            #print('forward')
        self.setCoords()            

    #Checks if the S key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def moveBackward(self, pressed, sprintCheck):
        if pressed[pygame.K_s] and sprintCheck:
            self.y += self.speed * self.sprint
        elif pressed[pygame.K_s]:
            self.y += self.speed
            #print('backward')

        self.setCoords()            

    #Checks if the D key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def moveRight(self, pressed, sprintCheck):
        if pressed[pygame.K_d] and sprintCheck:
            self.x += self.speed * self.sprint
        elif pressed[pygame.K_d]:
            self.x += self.speed
            #print('right')

        self.setCoords()

        

    #Checks if the A key has been pressed and if it has then it deducts 1 from the players coordinates and updates 
    #the coordintes of the player
    def moveLeft(self, pressed, sprintCheck):
        if pressed[pygame.K_a] and sprintCheck:
            self.x -= self.speed * self.sprint
        elif pressed[pygame.K_a]:
            self.x -= self.speed
            #print('left')    
        self.setCoords()


    def interact(self, pressed, map):
        if pressed[pygame.K_e]:
            #Uses a function which returns a list of the walls with items and gives it an identifier
            itemWalls = map.getItemWalls()
            #Goes through each one of these walls
            for itemWall in itemWalls:
                #Checks if the player's activation area has collided with the wall with an item, 
                #If the player's activation area has collided with the wall, they are close enough
                if self.activationArea.colliderect(itemWall.getRect()):
                    print(itemWall.getItem())



            '''coords = self.getMapCoords()
            wall = map.getObject(coords)
            hidingSpace = wall.getItem()
            print(hidingSpace)
            if isinstance(hidingSpace, objects.HidingSpace):

                print('THIS IS A HIDING SPACE')

            print('interact')'''

    def sprintCheck(self, pressed):
        if pressed[pygame.K_LSHIFT]:
            return True
        else: 
            return False

    #This changes the coordinates of the player whenever it is called, as the map coordinates of the player are directly linked to the 
    #screen coordinates of the player, by changing the screen coordinates (which moves the player image and rect) it also changes the
    #players location on the other map
    def setCoords(self):
        self.screenCoords = (self.x, self.y)
        self.hitbox.center = (self.x, self.y)
        self.setActivationCoords()
        #print(str(self.screenCoords))
    
    def getMapCoords(self):
        mapCoords = (round(self.x/32), round(self.y/32))
        return mapCoords
        x = round(int(self.screenCoords[0])/32)
        y = round(int(self.screenCoords[1])/32)
        self.mapCoords = (x, y)

    #This method checks if the W, A, S, D, E, or LEFT SHIFT buttons are pressed and then carries out various actions depending 
    #on the button that is pressed 
    def checkKeys(self, map):
        #Uses a pygame method to check if any key has been pressed and will be true if it is pressed and false if no buttons
        #on the keyboard are being pressed
        pressed = pygame.key.get_pressed()

        sprintCheck = self.sprintCheck(pressed)

        #Each of these methods control an aspect of the inputs from the user which in turn controls the player
        self.moveForward(pressed, sprintCheck)
        self.moveBackward(pressed, sprintCheck)
        self.moveRight(pressed, sprintCheck)
        self.moveLeft(pressed, sprintCheck)
        self.interact(pressed, map)

    def setActivationCoords(self):
        self.activationArea.center = self.hitbox.center
        #self.activationArea = pygame.Rect(self.x - 32, self.y - 32, self.width * 3, self.height * 3)
'''    #Returns the map coordinates of the player
    def getMapCoords(self):
        self.setMapCoords()
        return self.mapCoords'''





 

        