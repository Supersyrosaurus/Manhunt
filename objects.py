import pygame

pygame.init()

class Object():
    def __init__(self, x, y, height, width):
        #Each object has coordinates on the map
        self.xCoord = x
        self.yCoord = y
        #Each object needs height and width for display
        self.height = height
        self.width = width
        #Creates a surface using the height and width of the object which will be used to display the object
        self.surf = pygame.Surface([self.width, self.height])

    #Function returns the coordinates of the object
    def getCoords(self):
        return (self.xCoord, self.yCoord)

    #Procedure displays the object on the screen
    def display(self, screen):
        screen.blit(self.surf)


class Wall(Object):
    def __init__(self, x, y, height, width, type = None):
        super().__init__(x, y, height, width)
        #This sets the wall as 
        self.wall = self.setType()
        self.inputType = type

    def setType(self):
        #If type is none that means that there is nothing on the wall
        if self.inputType == None:
            return None
        #If type is 0 then that means that there is a hidingSpace on the wall
        if self.inputType == 0:
            pass
        #If type is 1 then that means that there is a lever on the wall
        if self.inputType == 1:
            pass
    
            
class Floor(Object):
    def __init__(self, x, y, height, width, type):
        super().__init__(x, y, height, width)
        self.type = type
        #Stores the level of sound for each floor object depending on the type of floor
        self.soundLevel = self.setSound()
    
    #Procedure sets the sound level depending on the type of the floor
    def setSound(self):
        if self.type == 'carpet':
            self.soundLevel = 0.2
            
        if self.type == 'concrete':
            self.soundLevel = 0.5
            
        if self.type == 'wood':
            self.soundLevel = 0.9
            
    #Function returns the sound level of the floor
    def checkSoundLevel(self):
        return self.soundLevel


class Lever(Object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self.activated = False
        #This is the activation area of the Lever, it will be a factor of the height and width (above one)
        self.area = pygame.Surface([self.activationWidth, self.activationHeight])
        self.activationArea = self.area.get_rect()
        self.activationHeight = height * 1
        self.activationWidth = width * 1

    #This checks if the player is within the activation area
    def inArea(self, playerRect):
        pass

    #Function checks if lever has been activated
    def checkLeverActivation(self):
        return self.activated

    #These 2 procedures change the self.activated attribute
    def activate(self):
        self.activated = True

    def deactivate(self):
        self.activated = False


class HidingSpace(Object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self.area = pygame.Surface([self.activationWidth, self.activationHeight])
        self.activationHeight = height * 1
        self.activationWidth = width * 1


    def inArea(self, playerLocation):
        pass

class Door(Object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self.activated = False

    #Function that returns whether the door has been activated
    def checkDoorActivation(self):
        return self.activated

    #Checks if the door should be activated depending on the max number of levers and how many have been activated
    def isActivated(self, activatedLevers, maxLevers):
        if activatedLevers == maxLevers:
            self.activated = True