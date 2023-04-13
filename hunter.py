import pygame
import sprite
import math
import physics
import random
pygame.init()

#class AStar():



class Hunter(sprite.Sprite):
    def __init__(self, x, y, img, scale, speed, sprintMultiplier):
        super().__init__(x, y, img, scale, speed, sprintMultiplier)
        self.soundProj = None
        self.soundProjSpeed = 16
        self.heard = False

        self.goalCoords = None
        self.visible = False

        self.sightProj = []
        self.seen = False

    def displayHunter(self, screen):
        self.displaySprite(screen)

    def pythagoras(self, x, y):
        xSqr = x**2
        ySqr = y**2
        dist = math.sqrt(xSqr + ySqr)

    #This method returns what values the xSpeed and ySpeed of the sound projectile should be
    def checkDirection(self, xDist, yDist):
        xSign = 0
        ySign = 0
        if xDist < 0:
            xSign = -1
        elif xDist > 0:
            xSign = 1
        if yDist < 0:
            ySign = -1
        elif yDist > 0:
            ySign = 1
        return xSign, ySign
    
    #This method takes in the absolute values for the x and y distances and then returns
    #the angle at which the projectile needs to be launched
    def angleCalcR(self, xDist, yDist):
        o = abs(yDist)
        a = abs(xDist)
        value = o/a
        angle = math.atan(value)
        return angle

    #This method takes the angle at which the projectile needs to be launched and
    #uses trigonometry in order to calculate what the x and y component need to be
    #in order for the projectile to move at a certain speed in that direction
    def speedCalcR(self, angle):
        xSpeed = 0
        ySpeed = 0
        projSpeed = self.soundProjSpeed
        cos = math.cos(angle)
        sin = math.sin(angle)
        xSpeed = projSpeed * cos
        ySpeed = projSpeed * sin
        return xSpeed, ySpeed
    
    
    #This method checks the number of walls between the player and the hunter
    def checkWalls(self, player, screen, map):
        xSpeed = 0
        ySpeed = 0
        #Checks if the sound projectile object has been created
        if self.soundProj == None:
            self.createSoundProjectile()
        if self.soundProj.getLaunched() == False or self.soundProj.getCollided() == True:
            self.soundProj.setCollided(False)
            #Sets the attribute for the sound projectile as a variable
            soundProj = self.soundProj
            #Gets the player coordiantes on the map
            pCoords = player.getCoords()
            #Calculates the distance between the player and the hunter in each axial direction
            coordDist = self.coordinateDistance(pCoords)
            xDist = coordDist[0]
            yDist = coordDist[1]
            direction = self.checkDirection(xDist, yDist)
            if xDist != 0 and yDist != 0:
                angle = self.angleCalcR(xDist, yDist)
                speeds = self.speedCalcR(angle)
                xSpeed = speeds[0] * direction[0]
                ySpeed = speeds[1] * direction[1]
            elif xDist == 0:
                xSpeed = 0
                ySpeed = self.soundProjSpeed * direction[1]
            elif yDist == 0:
                ySpeed = 0
                xSpeed = self.soundProjSpeed * direction[0]
            soundProj.setXSpeed(xSpeed)
            soundProj.setYSpeed(ySpeed)
            walls = soundProj.launchSoundProjectile(screen, self.getHitbox().center, map, player)
            return walls
        else:
            return
        
    #This method calculates the distance in each axis
    def coordinateDistance(self, coords):
        hCoords = self.getCoords()
        startX = coords[0]
        endX = hCoords[0]
        startY = coords[1]
        endY = hCoords[1]
        xDist = startX - endX
        yDist = startY - endY
        return xDist, yDist

    #This method calculates whether the hunter should be able to hear the player or not
    #and returns a boolean value based on that
    def sound(self, player, screen, map):
        maxSound = 100
        soundLevel = player.getSound()
        if isinstance(soundLevel, float) and player.getMovement():
            maxSound = soundLevel * maxSound
            wallNum = self.checkWalls(player, screen, map)
            maxSound -= wallNum
            if maxSound <= 50:
                return False
            elif maxSound <= 75:
                chance = random.randint(51, 75)
                if chance == maxSound:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def getHeard(self):
        return self.heard
    
    def setHeard(self, value):
        if value != True and value != False:
            print('INCORRECT VALUE FOR HEARD')
        self.heard = value

    #This method calculates the distance from the goal coordinates to the hunter by using the coordinates of the player and the hunter
    def hCost(self, coords):
        coordDist = self.coordinateDistance(coords)
        xDist = abs(coordDist[0])
        yDist = abs(coordDist[1])
        dist = self.pythagoras(xDist, yDist)
        return dist

    def setVisible(self, value):
        if value != True and value != False:
            print('NOT BOOLEAN VALUE FOR H VISIBILITY')
        self.visible = value

    def aStar(self, endCoords, map):
        fCost = 0
        gCost = 0
        hCost = self.hCost(endCoords)
        startCoords = self.getMapCoords()
        mapList = map.getMap()

    def createSoundProjectile(self):
        self.soundProj = physics.SoundProjectile(self.getHitbox().center, 0, 0, 1)
    
    def setSeen(self, value):
        if value != True and value != False:
            print('VALUE FOR SEEN IS NOT BOOLEAN')
        self.seen = value

    def getSeen(self):
        return self.seen

    def createSightProjectile(self):
        for x in range(0, 3):
            proj = physics.HunterSightProjectile(self.getHitbox().center, 0, 0, 32)
            self.sightProj.append(proj)

    def fov(self, screen, map, player):
        allWalls = map.getWalls()
        allWalls.append(player)
        projSpeed = 20
        if len(self.sightProj) == 0:
            self.createSightProjectile()
            print(self.sightProj)

        self.setProjDirection(projSpeed)
        for proj in self.sightProj:
            if proj.getCollided() == True or proj.getLaunched() == False:
                proj.setCollided(False)
                collided = proj.launchSightProjectile(screen, self.getHitbox().center, allWalls)
                print(proj.getPlayerCollision())
        self.setSeen(collided)
        


    def setProjDirection(self, projSpeed):
        if self.getBackward():
            #LEFT
            self.sightProj[0].setXSpeed(projSpeed * -1)
            self.sightProj[0].setYSpeed(projSpeed)
            #MIDDLE
            self.sightProj[1].setXSpeed(0)
            self.sightProj[1].setYSpeed(projSpeed)
            #RIGHT
            self.sightProj[2].setXSpeed(projSpeed)
            self.sightProj[2].setYSpeed(projSpeed)

        elif self.getRight():
            #TOP
            self.sightProj[0].setXSpeed(projSpeed)
            self.sightProj[0].setYSpeed(projSpeed * -1)
            #MIDDLE
            self.sightProj[1].setXSpeed(projSpeed)
            self.sightProj[1].setYSpeed(0)
            #BOTTOM
            self.sightProj[2].setXSpeed(projSpeed)
            self.sightProj[2].setYSpeed(projSpeed)

        elif self.getLeft():
            #TOP
            self.sightProj[0].setXSpeed(projSpeed * -1)
            self.sightProj[0].setYSpeed(projSpeed * -1)
            #MIDDLE
            self.sightProj[1].setXSpeed(projSpeed * -1)
            self.sightProj[1].setYSpeed(0)
            #BOTTOM
            self.sightProj[2].setXSpeed(projSpeed * -1)
            self.sightProj[2].setYSpeed(projSpeed)

        else:
            #LEFT
            self.sightProj[0].setXSpeed(projSpeed * -1)
            self.sightProj[0].setYSpeed(projSpeed * -1)
            #MIDDLE
            self.sightProj[1].setXSpeed(0)
            self.sightProj[1].setYSpeed(projSpeed * -1)
            #RIGHT
            self.sightProj[2].setXSpeed(projSpeed)
            self.sightProj[2].setYSpeed(projSpeed * -1)

    def randomMove(self):
        x = random.randint(1, 4)
        if x == 1:
            self.moveForward()
        if x == 2:
            self.moveBackward()
        if x == 3:
            self.moveRight()
        if x == 4:
            self.moveLeft()


    def ready(self, screen, map, player):
        self.setCoords()
        if self.visible == True:
            self.displayHunter(screen)
        heard = self.sound(player, screen, map)
        self.setHeard(heard)
        self.fov(screen, map, player)
        #print(self.getSeen())
        self.randomMove()
        self.checkCollision(map)
        
        '''walls = self.checkWalls(player, screen, map)
        print(str(walls))'''




































