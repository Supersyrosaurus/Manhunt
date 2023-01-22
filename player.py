import pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        
        coords = (x, y)
        self.playerImg = pygame.image.load('whiteCircle.png').convert_alpha()
        self.playerHitbox = self.playerImg.get_rect()
        self.forward = False
        self.back = False
        self.left = False
        self.right = False

    def checkMovement(self):
