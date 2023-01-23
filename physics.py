import pygame
pygame.init()

class Physics():
    def __init__(self):
        pass

    def checkCollision(self, objOne, objTwo):

        return objOne.colliderect(objTwo)
        



class Projectile(Physics, pygame.sprite.Sprite):
    def __init__(self, coords, xSpeed, ySpeed, height, width):
        super().__init__()
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.coords = coords
        self.rect = pygame.Rect(coords[0], coords[1], width, height)

    def launchProjectile(self, screen):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

        if self.rect.right >= screen.getWidth() or self.rect.left <= 0:
            self.xSpeed *= -1
        if self.rect.bottom >= screen.getHeight() or self.rect.top <= 0:
            self.ySpeed *= -1

        pygame.draw.rect(screen.getScreen(), (0,0,0), self.rect)
        