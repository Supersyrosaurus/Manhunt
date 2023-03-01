import pygame
import math
import objects
import screens
import colours
pygame.init()

class Physics():
    def __init__(self):
        pass

    def checkCollision(self, objOne, objTwo):

        return objOne.colliderect(objTwo)
        
    def pythagoras(self, numOne, numTwo):
        squared = (numOne ** 2) + (numTwo ** 2)
        squareRoot = math.sqrt(squared)
        return squareRoot



class Projectile():
    def __init__(self, coords, xSpeed, ySpeed, length):
        super().__init__()
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.coords = coords
        self.rect = pygame.Rect(coords[0], coords[1], length, length)
        self.collided = False
        self.launched = False

    def getLaunched(self):
        return self.launched

    def getCollided(self):
        return self.collided
    
    def collideCheck(self, object):
        return self.rect.colliderect(object)
    
    def setCollided(self, value):
        self.collided = value
    
    def moveProjectile(self, screen):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

        #pygame.draw.rect(screen.getScreen(), colours.red, self.rect)

    
    '''def xCollide(self):
        self.xSpeed *= -1

    def yCollide(self):
        self.ySpeed *= -1
    def launchProjectile(self, screen):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

        if self.rect.right >= screen.getWidth() or self.rect.left <= 0:
            self.xCollide()
        if self.rect.bottom >= screen.getHeight() or self.rect.top <= 0:
            self.yCollide()

        pygame.draw.rect(screen.getScreen(), (0,0,0), self.rect)'''
        
class SightProjectile(Projectile):
    def __init__(self, coords, xSpeed, ySpeed, length):
        super().__init__(coords, xSpeed, ySpeed, length)
        self.collidedObjects = []

    
    def getCollidedObjects(self):
        return self.collidedObjects
    

    def searchObjects(self, searchObject):
        found = False
        for object in self.collidedObjects:
            if object == searchObject:
                found = True
        return found
    
    def objectCheck(self, allObjects):
        for object in allObjects:
            rect = object.getRect()
            if self.collideCheck(rect) == True:
                #print(self.collideCheck(rect))
                self.collidedObjects.append(object)
                object.setVisible(True)
                if isinstance(object, objects.Wall) or isinstance(object, objects.Door):
                    self.collided = True
            #elif self.searchObjects(object) == False:
                #object.setVisible(False)
            

    def launchSightProjectile(self, screen, map, coords):
        self.collidedObjects = []
        allObjects = map.getAllObjects()
        self.rect.center = coords
        self.launched = True
        while self.collided == False:
            self.moveProjectile(screen)
            self.objectCheck(allObjects)
        return self.collidedObjects
        
        
        

class SoundProjectile(Projectile):
    def __init__(self, coords, xSpeed, ySpeed, length):
        super().__init__(coords, xSpeed, ySpeed, length)
        self.wallNum = 0

    def launchSoundProjectile(self):
        pass
        
