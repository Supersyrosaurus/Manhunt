import pygame
import sprite
import math
import physics
pygame.init()

#class AStar():



class Hunter(sprite.Sprite):
    def __init__(self, x, y, img, scale, speed, sprintMultiplier):
        super().__init__(x, y, img, scale, speed, sprintMultiplier)
        self.soundProj = None

    def displayHunter(self, screen):
        self.displaySprite(screen)

    def pythagoras(self, x, y):
        xSqr = x**2
        ySqr = y**2
        dist = math.sqrt(xSqr + ySqr)

    #This method checks the number of walls between the player and the hunter
    def checkWalls(self, player, screen, map):
        #Checks if the sound projectile object has been created
        if self.soundProj == None:
            self.createSoundProjectile()
        #Sets the attribute for the sound projectile as a variable
        soundProj = self.soundProj
        #Gets the player coordiantes on the map
        pCoords = player.getMapCoords()
        #Calculates the distance between the player and the hunter in each axial direction
        coordDist = self.coordinateDistance(pCoords)
        print(coordDist)
        xSpeed = 0
        ySpeed = 0
        #Sets the speed of the sound projectile based on which direction the player is in
        if coordDist[0] < 0:
            xSpeed = -5
        else:
            xSpeed = 5
        if coordDist[1] < 0:
            ySpeed = -5
        else:
            ySpeed = 5
        print(xSpeed)
        print(ySpeed)
        soundProj.setXSpeed(xSpeed)
        soundProj.setYSpeed(ySpeed)
        #Runs a method on the sound projectile which returns the number of walls the projectile has collided with
        walls = soundProj.launchSoundProjectile(screen, self.getHitbox().center, map, player)
        return walls

    #This method calculates the distance in each axis
    def coordinateDistance(self, coords):
        hCoords = self.getMapCoords()
        print(coords)
        print(hCoords)
        startX = coords[0]
        endX = hCoords[0]
        startY = coords[1]
        endY = hCoords[1]
        xDist = startX - endX
        yDist = startY - endY
        return xDist, yDist


    #This method calculates the distance from the goal coordinates to the hunter by using the coordinates of the player and the hunter
    def hCost(self, coords):
        coordDist = self.coordinateDistance(coords)
        xDist = abs(coordDist[0])
        yDist = abs(coordDist[1])
        dist = self.pythagoras(xDist, yDist)
        return dist

    

    def aStar(self, endCoords, map):
        fCost = 0
        gCost = 0
        hCost = self.hCost(endCoords)
        startCoords = self.getMapCoords()
        mapList = map.getMap()

    def createSoundProjectile(self):
        self.soundProj = physics.SoundProjectile(self.getHitbox().center, 0, 0, 32)
    
    def ready(self, screen, map, player):
        self.setCoords()
        self.displayHunter(screen)
        self.checkWalls(player, screen, map)




































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
