import pygame
import sprite
import math
pygame.init()

class AStar():



class Hunter(sprite.Sprite):
    def __init__(self, x, y, img, scale, speed, sprintMultiplier, map):
        super().__init__(x, y, img, scale, speed, sprintMultiplier)

    def displayHunter(self, screen):
        self.displaySprite(screen)

    def pythagoras(self, x, y):
        xSqr = x**2
        ySqr = y**2
        dist = math.sqrt(xSqr + ySqr)

    #This method calculates the distance from the goal coordinates to the hunter by using the coordinates of the player and the hunter
    def hCost(self, coords):
        hCoords = self.getMapCoords()
        gx = coords[0]
        hx = hCoords[0]
        gy = coords[1]
        hy = hCoords[1]
        xDist = abs(gx-hx)
        yDist = abs(gy-hy)
        dist = self.pythagoras(xDist, yDist)
        return dist



    def aStar(self, endCoords, map):
        fCost = 0
        gCost = 0
        hCost = self.hCost(endCoords)
        startCoords = self.getMapCoords()
        mapList = map.getMap()







































'''  def moveForward(self):
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
'''
