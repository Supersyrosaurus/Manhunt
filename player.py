import pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__
        self.x = x
        self.y = y
        self.screenCoords = (x, y)
        self.mapCoords = (self.screenCoords[0]/32, self.screenCoords[1]/32)
        self.img = pygame.image.load(img).convert_alpha()
        self.hitbox = self.img.get_rect()
        self.hiding = False

    def displayPlayer(self, screen):
        screen.blit(self.img, self.screenCoords)

    def moveForward(self):
        self.y -= 1
        print(self.y)

    def moveBackward(self):
        self.y += 1
        #print(self.y)
    def moveRight(self):
        self.x += 1
        #print(self.x)
    def moveLeft(self):
        self.x -= 1
        print(self.x)
        
    def setCoords(self):
        self.screenCoords = (self.x, self.y)
        print(str(self.screenCoords))

    def checkMove(self, canPress):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.moveForward()
            self.setCoords()
            canPress = False
            print('forward')
        if pressed[pygame.K_s]:
            self.moveBackward()
            self.setCoords()
            canPress = False
            print('backward')
        if pressed[pygame.K_d]:
            self.moveRight()
            self.setCoords()
            canPress = False
            print('right')
        if pressed[pygame.K_a]:
            self.moveLeft()
            self.setCoords()
            canPress = False
            print('left')


 

        