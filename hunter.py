import pygame
import sprite
import math
import physics
import random
import objects
pygame.init()

#class AStar():



class Hunter(sprite.Sprite):
    def __init__(self, x, y, img, scale, speed, sprintMultiplier):
        super().__init__(x, y, img, scale, speed, sprintMultiplier)
        self.soundProj = None
        self.soundProjSpeed = 16
        self.heard = False

        self.visible = False

        self.sightProj = []
        self.seen = False

        self.firstMove = False

        self.path = None
        self.pathIndex = 0

        self.chasing = False

    def displayHunter(self, screen):
        self.displaySprite(screen)

    def pythagoras(self, x, y):
        xSqr = x**2
        ySqr = y**2
        dist = math.sqrt(xSqr + ySqr)
        return dist

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

    def calcDistance(self, player):
        playerCoords = player.getCoords()
        xDist, yDist = self.coordinateDistance(playerCoords)
        dist = self.pythagoras(xDist, yDist)
        return dist

    #This method calculates whether the hunter should be able to hear the player or not
    #and returns a boolean value based on that
    def sound(self, player, screen, map):
        maxSound = 100
        soundLevel = player.getSound()
        dist = self.calcDistance(player)
        if dist > 600:
            return False
        if isinstance(soundLevel, float) and player.getMovement():
            maxSound = soundLevel * maxSound
            wallNum = self.checkWalls(player, screen, map)
            maxSound -= wallNum
            if maxSound <= 50:
                self.setHeard(False)
            elif maxSound <= 75:
                chance = random.randint(51, 75)
                if chance == maxSound:
                    self.setHeard(True)
                else:
                    self.setHeard(False)
            else:
                self.setHeard(True)
        else:
            self.setHeard(False)

    def getHeard(self):
        return self.heard
    
    def setHeard(self, value):
        if value != True and value != False:
            print('INCORRECT VALUE FOR HEARD')
        self.heard = value

    def setVisible(self, value):
        if value != True and value != False:
            print('NOT BOOLEAN VALUE FOR H VISIBILITY')
        self.visible = value

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
            #print(self.sightProj)

        self.setProjDirection(projSpeed)
        for proj in self.sightProj:
            if proj.getCollided() == True or proj.getLaunched() == False:
                proj.setCollided(False)
                collided = proj.launchSightProjectile(screen, self.getHitbox().center, allWalls)
                #print(proj.getPlayerCollision())
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

    #This method runs a method on all of the objects in the map to calculate the hCost
    #for each object from that object to the end goal coordinates
    def calcHCost(self, map, endCoords):
        allFloors = map.getFloors()
        for floor in allFloors:
            floor.reset()
            floor.calcHCost(endCoords)

    #This is the code for the A* algorithm for the hunter to use
    def aStar(self, endCoords, map):
        #This variable is for whether the point has been found
        found = False
        #These are the open and closed lists for the nodes
        open = []
        closed = []
        #The start node is wherever the hunter is
        startCoords = self.getMapCoords()
        startNode = map.getObject(startCoords)
        #This method is run in order to determine the H cost for every node to the endpoint
        self.calcHCost(map, endCoords)
        #As the start node is no distance from itself, the gCost for it is 0
        startNode.setGFCost(0)
        #The start node is added to the open list as its the first one to be considered
        open.append(startNode)
        #print(open)

        #This loop runs while the endpoint has not been found
        while found == False:
            #print('doingB')
            #Current is the lowest f cost in the open list,
            #This must be a high number so that it does not interfere with actual f costs
            lowestF = 10000000
            current = None            
            #This loops through each element in the open list
            for x in range(len(open)):
                #print('doingO')
                #Checks if the f cost of the current node is greater than any other nodes in the open
                #list and if it is then the node with the lower f cost is set as the current
                if open[x].getFCost() < lowestF:
                    current = open[x]
                    lowestF = current.getFCost()
                    index = x
            #After the node with the lowest fCost is found then the node is added to the closed list
            closed.append(current)
            #print(current)
            #and deleted from the open list
            del open[index]
            #print(open)
            #print(closed)

            #This checks if the current node is the node which we are looking for
            #If it is then the loop will be broken
            if current.getCoords() == endCoords:
                #print(current.getCoords())
                found = True
            
            
            #This goes through each of the neighbours of the current node
            for node in self.getNeighbours(current, map):
                #print('doingN')
                #This checks if the node is an object of type floor and that it is not already in closed
                if isinstance(node, objects.Floor) and self.checkClosed(closed, node):
                    #This sets the last node for the neighbour node as the current
                    node.setLast(current)
                    #This sets the g and f cost of the node now based on the last node
                    node.setGFCost()
                    #This checks if the node 
                    open.append(node)
        return current
            
    #This method is a recursive algorithm which goes which goes through
    #each node in the path and gets the previous node by invoking the same function
    def findPath(self, endNode):
        #Base case - if g cost is 0 it must be the place where we began
        if endNode.getGCost() == 0:
            return [endNode]
        endNode.path = True
        list = self.findPath(endNode.getLast())
        list.append(endNode)
        return list


    #This method takes a node on the map and returns the neighbours of the node
    def getNeighbours(self, node, map):
        coords = node.getCoords()
        cOne = (coords[0] - 1, coords[1])
        cTwo = (coords[0] + 1, coords[1])
        cThree = (coords[0], coords[1] - 1)
        cFour = (coords[0], coords[1] + 1)
        nOne = map.getObject(cOne)
        nTwo = map.getObject(cTwo)
        nThree = map.getObject(cThree)
        nFour = map.getObject(cFour)
        neighbours = [nOne, nTwo, nThree, nFour]
        return neighbours

    #This method checks whether a node is already in the closed list
    def checkClosed(self, closed, current):
        for node in closed:
            if node == current:
                return False
        return True

    #This method takes the list created from the A* algorithm and then
    #rearranges it it so that the start node is first in the list
    def rearrangePathList(self, list):
        newList = []
        for x in range(len(list)):
            index = len(list) - x
            newList.append(list[index])
        return newList

    #This method checks the hunter's positition relative to a node
    #and based on that moves in a specific direction
    def traverse(self, node, map):
        hCoords = self.getHitbox().center
        gCoords = node.getRect().center
        xH, yH = hCoords
        xG, yG = gCoords
        xDir = xH - xG
        yDir = yH - yG
        #print(hCoords)
        #print(gCoords)
        if xDir > 0:
            #for x in range(loop):
            self.moveLeft()
            self.setCoords()
            self.checkCollision(map)
        if xDir < 0:
            #for x in range(loop):
            self.moveRight()
            self.setCoords()
            self.checkCollision(map)
        if yDir > 0:
            #for x in range(loop):
            self.moveForward()
            self.setCoords()
            self.checkCollision(map)
        if yDir < 0:
            #for x in range(loop):
            self.moveBackward()
            self.setCoords()
            self.checkCollision(map)
        #print(self.getCoords())

    #This is the overarching method for the pathfinding algorithm which includes the movement and the calculations
    def pathfind(self, endCoords, map):
        print(map.getObject(endCoords))
        print(endCoords)
        endNode = self.aStar(endCoords, map)
        self.path = self.findPath(endNode)
        self.pathIndex = 0
        #print('path:')
        #print(self.path)

    #This method checks whether the hunter has a path to follow or not 
    #and based on this it either makes the hunter follow that path or 
    #reset the variables for another path
    def followPath(self, map):
        if self.pathIndex < len(self.path):
            node = self.path[self.pathIndex]
            self.traverse(node, map)
            nodeCoords = node.getRect().center
            if nodeCoords == self.getCoords():
                self.pathIndex += 1
            #print(self.pathIndex)
        else:
            self.path = None

    #This method checks whether the hunter needs to create a new path or not and
    #it also checks if the hunter has either seen or heard the player.
    def checkPath(self, map, player):
        hiding = player.getHiding()
        if self.path != None:
            if (self.heard == True or self.seen == True) and hiding == False and self.getChasing() == False:
                endCoords = player.getMapCoords()
                self.pathfind(endCoords, map)
                self.setChasing(True)
        else:
            self.setChasing(False)
            self.randomPath(map)
        self.followPath(map) 

    #This method generates a random path for the hunter to follow
    def randomPath(self, map):
        floors = map.getFloors()
        index = random.randint(0, (len(floors) - 1))
        floor = floors[index]
        endCoords = floor.getCoords() 
        self.pathfind(endCoords, map)

    #This method checks if the hunter has won the game
    def checkWin(self, player):
        pRect = player.getHitbox()
        hRect = self.getHitbox()
        if hRect.colliderect(pRect) and player.getHiding() == False:
            return True

    def getChasing(self):
        return self.chasing
    
    def setChasing(self, value):
        self.chasing = value

    def ready(self, screen, map, player):
        self.setCoords()
        #if self.visible == True:
        self.displayHunter(screen)
        self.sound(player, screen, map)
        self.fov(screen, map, player)
        self.checkPath(map, player)
        win = self.checkWin(player)
        if win == True:
            return True
        
        #print(self.getSeen())
        #self.randomMove()
        #self.checkCollision(map)
        




































