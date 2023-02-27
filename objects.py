import pygame
import physics
import colours

pygame.init()

class Object(physics.Physics):
    def __init__(self, Coords):
        #Each object has coordinates on the map
        self.Coords = Coords
        #Creates a rect using the height and width of the object which will be used to display the object
        self.rect = pygame.Rect(self.Coords[0] * 32, self.Coords[1] * 32, 32, 32)
        #This is the center cooridnates of the object on the screen
        self.center = self.rect.center

    #Function returns the coordinates of the object
    def getCoords(self):
        return self.Coords

    def getRect(self):
        return self.rect

    def getCenter(self):
        return self.center
    

'''    #Procedure displays the object on the screen
    def display(self, screen, colour):
        pygame.draw.rect(screen, colour, self.rect)
'''

class Wall(Object):
    def __init__(self, Coords, type = None):
        super().__init__(Coords)
        self.type = type
        #This sets the wall as 
        self.item = self.setItem()
        self.colour = self.setColour()


    def setItem(self):
        #If type is none that means that there is nothing on the wall
        if self.type == 'empty':
            return None

        #If type is 0 then that means that there is a hidingSpace on the wall
        if self.type == 'hidingSpace':
            return HidingSpace(self.Coords)
            
        #If type is 1 then that means that there is a lever on the wall
        if self.type == 'lever':
            return Lever(self.Coords)

    def getItem(self):
        return self.item
    
    def setColour(self):
        #If type is none that means that there is nothing on the wall
        if self.type == 'empty':
            return colours.black

        #If type is 0 then that means that there is a hidingSpace on the wall
        if self.type == 'hidingSpace':
            return colours.blue

        #If type is 1 then that means that there is a lever on the wall
        if self.type == 'lever':
           return colours.green

    def getColour(self):
        return self.colour
    
            
    
            
class Floor(Object):
    def __init__(self, Coords, type):
        super().__init__(Coords)
        self.type = type
        #Stores the level of sound for each floor object depending on the type of floor
        self.soundLevel = self.setSound()
        self.colour = self.setColour()
    
    #Procedure sets the sound level depending on the type of the floor
    def setSound(self):
        if self.type == 'carpet':
            return 0.2
            
        if self.type == 'concrete':
            return 0.5
            
        if self.type == 'wood':
            return 0.9
            
    #Function returns the sound level of the floor
    def getSoundLevel(self):
        return self.soundLevel
    
    def getType(self):
        return self.type
    
    def setColour(self):
        #If type is none that means that there is nothing on the wall
        if self.type == 'carpet':
            return colours.navy

        #If type is 0 then that means that there is a hidingSpace on the wall
        if self.type == 'concrete':
            return colours.lightGrey

        #If type is 1 then that means that there is a lever on the wall
        if self.type == 'wood':
           return colours.green
        
    def getColour(self):
        return self.colour


class Lever(Object):
    def __init__(self, Coords):
        super().__init__(Coords)
        self.activated = False



    #Function checks if lever has been activated
    def getActivated(self):
        return self.activated

    #These 2 procedures change the self.activated attribute
    def activate(self):
        self.activated = True

    def deactivate(self):
        self.activated = False


class HidingSpace(Object):
    def __init__(self, Coords):
        super().__init__(Coords)
        self.activationArea = pygame.Rect((self.Coords[0] - 1) * 32, (self.Coords[1]) * 32, 96, 96)


    def inArea(self, playerHitbox):
        check = self.checkCollision(playerHitbox, self.activationArea)
        return check
        

class Door(Object):
    def __init__(self, Coords):
        super().__init__(Coords)
        self.activated = False
        self.colour = colours.lightBrown

    #Function that returns whether the door has been activated
    def checkDoorActivation(self):
        return self.activated

    #Checks if the door should be activated depending on the max number of levers and how many have been activated
    def activate(self):
        self.activated = True

    def getActivated(self):
        return self.activated
    
    def getColour(self):
        return self.colour


#########################       UNUSED CODE         ###################


'''#This checks if the player is within the activation area
def inArea(self, playerRect):
    pass'''