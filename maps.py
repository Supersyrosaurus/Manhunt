import pygame
import objects

pygame.init()

class Map():
    #walls and floors are passed as dictionaries where the key
    #corresponds to the type of each and also includes the coordinates
    #door is passed as just coordinates 
    #The coordinates in each of these are not the display coordinates but
    #the grid coordinates
    def __init__(self, walls, floors, doorCoord, mapWidth, mapHeight):
        #doorCoord is the coordinates of the node with the door
        #not the display coordinates
        doorCoord = doorCoord
        #This is passed as a dictionary which contains the number of each of the walls it should create
        #and the coordinates for each of the nodes on the map
        self.walls = walls
        #This is also passed as a dictionary with similar things
        self.floors = floors
        self.map = []
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight


    def createMap(self):

    def addMapHeight(self):
        for x in range(self.mapHeight):
            self.map.append([])

    def createNode(self):
    
    def addFloors(self):

    def addWalls(self):

    def outerWallsandDoor
        
        


class Node():
    def __init__(self, x, y, category, type):
        self.x = x
        self.y = y
        self.object = self.addObject(category, type)

    def addObject(self, category, type):
        if category == 'walls':
            pass

        elif category == 'floors':
            return objects.Floor(self.x, self.y)

        else:
            return objects.Door(self.x, self.y)

        
        

