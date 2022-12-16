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

    def createNode(self):
        
        


class Node():
    def __init__(self):
