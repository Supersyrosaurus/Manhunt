import pygame
pygame.init()

class Hunter():
    def __init__(self, x, y, img, scale, speed, sprintMultiplier, map):
        super().__init__
        #Coordinate attributes
        self.x = x
        self.y = y
        self.mapCoords = self.setMapCoords()
        #Image attributes
        self.img = pygame.image.load(img).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height()
        self.transformedImg = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))
        self.width = self.transformedImg.get_width()
        self.height = self.transformedImg.get_height()
        #Hitbox of the player by creating a rectangle around the player img
        self.hitbox = self.transformedImg.get_rect()
        self.speed = speed
        self.sprintMultiplier = sprintMultiplier
        self.map = map
        self.forward = False
        self.left = False
        self.right = False
        self.backward = False
        self.sprinting = False

    def displayHunter(self, screen):
        screen.blit(self.transformedImg, self.hitbox.topleft)


    def moveForward(self):
        if self.getSprinting() == True:
            self.y -= self.speed * self.sprintMultiplier
        else:
            self.y -= self.speed
        self.forward = True

    def moveBackward(self):
        if self.getSprinting() == True:
            self.y += self.speed * self.sprintMultiplier
        else:
            self.y += self.speed
        self.backward = True

    def moveLeft(self):
        if self.getSprinting() == True:
            self.x -= self.speed * self.sprintMultiplier
        else:
            self.x -= self.speed
        self.left = True

    def moveRight(self):
        if self.getSprinting() == True:
            self.x += self.speed * self.sprintMultiplier
        else:
            self.x -= self.speed
        self.right = True

    def getSprinting(self):
        return self.sprinting
    
    def setSprinting(self, value):
        self.sprinting = value

