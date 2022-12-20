import pygame
import objects

pygame.init()

class Map():
    #walls and floors are passed as dictionaries where the key
    #corresponds to the type of each and also includes the coordinates
    #door is passed as just coordinates 
    #The coordinates in each of these are not the display coordinates but
    #the grid coordinates
    def __init__(self, walls, floors, doorCoord, mapLength):
        #doorCoord is the coordinates of the node with the door
        #not the display coordinates
        self.doorCoord = doorCoord
        #This is passed as a dictionary which only contains the coordinates of
        #Each type of wall 
        self.walls = walls
        #This is also passed as a dictionary with similar things
        self.floors = floors
        self.map = []
        #As there needs to be an outer border of empty walls, 
        #The real height and width of the map will need to be increased by 2
        self.mapLength = mapLength + 2


    def createEmptyMap(self):
        for y in range(self.mapLength):
            self.map.append([])
            for x in range(self.mapLength):
                print(str(x))
                if y == 0 or y == self.mapLength - 1:
                    wall = objects.Wall(x, y)
                    self.map[y].append('W')
                elif x == 0 or x == self.mapLength - 1:
                    wall = objects.Wall(x, y)
                    self.map[y].append('W')
                else:
                    self.map[y].append(0)            
        


'''class Node():
    def __init__(self):'''
