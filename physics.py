import pygame
pygame.init()

class Physics():
    def __init__(self):
        pass

    def changeSpeed(self,rect, xSpeed, ySpeed, screen):
        rect.x += xSpeed
        rect.y += ySpeed
        pygame.draw.rect(screen, (0,0,0), rect)



    def checkCollision(self, objOne, objTwo):
        return objOne.colliderect(objTwo)
        



class Projectile(Physics):
    def __init__(self, coords, speed, height, width):
        self.speed = speed
        self.rect = pygame.Rect(coords[0], coords[1], width, height)
        