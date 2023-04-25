import pygame
import math
import objects
import hunter
import colours
import player
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


#Parent class for sight projectiles and sound projectiles
class Projectile():
    def __init__(self, coords, xSpeed, ySpeed, length):
        super().__init__()
        #Control the speed of the projectile
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        #Origin coordinates of the projectile
        self.coords = coords
        #This is the actual rect for the projectile, created using pygame library
        self.rect = pygame.Rect(coords[0], coords[1], length, length)
        #This is a boolean value which is whether the projecitle has collided with a wall or not
        self.collided = False
        #This is a boolean value which is whether the projectile has been launched or not
        self.launched = False

    #This is a get function which returns the value for the launched attribute
    def getLaunched(self):
        return self.launched

    #This is the get function returning the value for the collided attribute
    def getCollided(self):
        return self.collided
    
    #This is a function that checks if an object passed has collided with itself
    def collideCheck(self, object):
        return self.rect.colliderect(object)
    
    #This is a procedure that sets the value of the collided attribute as a
    #value passed to the procedure
    def setCollided(self, value):
        if value == True or value == False:
            self.collided = value
    
    #This is the procedure that moves the projectile, screen is for testing purposes
    def moveProjectile(self, screen):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

    #This method changes the x speed of the projectile to whatever is passed into the method 
    def setXSpeed(self, value):
        if isinstance(value, float) == False and isinstance(value, int) == False:
            print('NOT AN INTEGER VALUE FOR XSPEED')
        self.xSpeed = value
    
    #This method changes the y speed of the projectile to whatever is passed into the method
    def setYSpeed(self, value):
        if isinstance(value, float) == False and isinstance(value, int) == False:
            print('NOT AN INTEGER VALUE FOR YSPEED')
        self.ySpeed = value

    def displayProjectile(self, screen):
        pygame.draw.rect(screen, colours.red, self.rect)

#This is the class for sight projectiles, which inherits projectile
class SightProjectile(Projectile):
    def __init__(self, coords, xSpeed, ySpeed, length):
        super().__init__(coords, xSpeed, ySpeed, length)
        #This attribute is a list which will contain all of the objects that the projectile has
        #Collided with
        self.collidedObjects = []

    #This returns a list of all of the objects which the projectile has collided with 
    def getCollidedObjects(self):
        return self.collidedObjects
    
    #This is a method that searches through all of the objects in order to check
    #If the projectile has collided with it
    def searchObjects(self, searchObject):
        found = False
        for object in self.collidedObjects:
            if object == searchObject:
                found = True
        return found
    
    #This method checks if the projectile has collided with any of the objects in the map
    #and based on that is sets the visibility as True and if it is a wall then it sets 
    #The collided attribute as true
    def objectCheck(self, allObjects):
        #Goes through all of the objects in the map
        for object in allObjects:
            if isinstance(object, hunter.Hunter):
                rect = object.getHitbox()
            else:
                rect = object.getRect()
            #Method invoked with that object above passed to check if the projectile has
            #collided with it
            if self.collideCheck(rect) == True:
                #If it has then it is added to the collided objects list
                self.collidedObjects.append(object)
                #The visibility of that object is set to True so it can be seen
                object.setVisible(True)
                #Checks if the object is a door or a wall and if it is then it has collided so collided is True
                if isinstance(object, objects.Wall) or isinstance(object, objects.Door):
                    self.collided = True

    #This method launches the projectile and then runs the other methods in order to check
    #what objects the projectile has collided with and returns the list of objects the projecile
    #Has collided with
    def launchSightProjectile(self, screen, allObjects, coords):
        #Sets the collided objects as an empty list each time the projectile is launched
        self.collidedObjects = []
        #The center of the projectile is set as the coordinates passed
        self.rect.center = coords
        self.launched = True
        #Runs while the projectile has not collided with a wall or door
        while self.collided == False:
            self.moveProjectile(screen)
            self.objectCheck(allObjects)
        #Once it has collided with a wall or door then self.collided will be true
        #So list of all collided objects are returned
        return self.collidedObjects
        
        
class HunterSightProjectile(Projectile):
    def __init__(self, coords, xSpeed, ySpeed, length):
        super().__init__(coords, xSpeed, ySpeed, length)
        self.playerCollision = False

    #This method checks if the projectile has collided with any walls or the player
    #and if it has then it returns the collided attribute as True and 
    #if the projectile has collided with the player then the playerCollision attribute is
    #also set as True
    def checkCollisions(self, allWalls):
        for wall in allWalls:
            if isinstance(wall, player.Player):
                rect = wall.getHitbox()
            else:
                rect = wall.getRect()
        
            if self.collideCheck(rect):
                if isinstance(wall, player.Player):
                    self.collided = True
                    self.playerCollision = True
                else:
                    self.collided = True

    #This method is very similar to the original sight projectile method
    def launchSightProjectile(self, screen, coords, allWalls):
        self.rect.center = coords
        self.launched = True
        self.playerCollision = False
        while self.collided == False:
            self.moveProjectile(screen)
            self.displayProjectile(screen)
            self.checkCollisions(allWalls)
        return self.playerCollision

    #This metho just returns the playerCollision attribute
    def getPlayerCollision(self):
        return self.playerCollision
    



#This is the sound projectile class which will be used by the hunter to determine the number of walls between the player and the hunter
class SoundProjectile(Projectile):
    def __init__(self, coords, xSpeed, ySpeed, length):
        super().__init__(coords, xSpeed, ySpeed, length)
        #This attribute will be used to record the number of wall which the projectile has collided into
        self.wallNum = 0
        self.collidedWalls  = []

    #This method checks if the projectile has collided into the player by taking the player's hitbox as a parameter
    def playerCollision(self, player, screen):
        if self.collideCheck(player.getHitbox()) or self.rect.x < 0 or self.rect.x > 960 or self.rect.y < 0 or self.rect.y > 640:
            self.setCollided(True)
            return
        self.setCollided(False)

    #This method launches the sound projectile and then returns the number of walls the projecitle has collided into
    def launchSoundProjectile(self, screen, coords, map, player):
        self.wallNum = 0
        self.launched = True
        self.rect.center = coords
        walls = map.getWalls()
        while self.collided == False:
            self.moveProjectile(screen)
            self.wallCheck(walls)
            self.playerCollision(player, screen)
        collidedNum = self.wallNum
        self.collidedWalls = []
        #self.wallNum = 0
        return collidedNum
    
    #This method checks if the projectile has collided with a wall in the map and if it has then it increments the number of walls collided
    def wallCheck(self, walls):
        for wall in walls:
            if self.collideCheck(wall) == True and self.alreadyCollided(wall) == False:
                self.wallNum += 1
                self.collidedWalls.append(wall)
            
    def alreadyCollided(self, check):
        for wall in self.collidedWalls:
            if check == wall:
                return True
        return False