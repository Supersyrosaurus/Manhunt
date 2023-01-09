import pygame
pygame.init()

class Player():
    def __init__(self, x, y):
        coords = (x, y)
        self.playerImg = pygame.image.load('whiteCircle.png').convert_alpha()
        self.playerHitbox = self.playerImg.get_rect()
        self.forward = False
        self.back = False
        self.left = False
        self.right = False

    def checkMovement(self):
