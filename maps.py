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
        self.borderWalls = []
        #This is also passed as a dictionary with similar things
        self.floors = floors
        self.map = []
        #As there needs to be an outer border of empty walls, 
        #The real height and width of the map will need to be increased by 2
        self.mapLength = mapLength + 2

    def getMap(self):
        return self.map

    #Uses the different methods within the class to create a map
    def createMap(self):
        self.createEmptyMap()
        self.addWalls()
        self.addFloors()
        self.addDoor()
    
    #Creates an empty shell for the map with an outer border of walls and empty spaces in the middle
    def createEmptyMap(self):
        #Loops for as long as the length of the map is
        for y in range(self.mapLength):
            #for every loop a new list is appended
            self.map.append([])
            for x in range(self.mapLength):
                #for every loop a new element is appended to the new list
                if y == 0 or y == self.mapLength - 1:
                    #This if statement checks if it is the first list or the last list
                    #and if it is it fills it with wall objects 
                    wall = objects.Wall((x, y))
                    self.map[y].append(wall)
                    self.borderWalls.append((x,y))
                elif x == 0 or x == self.mapLength - 1:
                    #This checks if the element is the first or the last
                    #and if it is then it appends a wall object instead 
                    wall = objects.Wall((x, y))
                    self.map[y].append(wall)
                    self.borderWalls.append((x,y))
                else:
                    #This appends an empty spot in the list
                    self.map[y].append(0)            
    
    #Adds the inner walls to the map     
    def addWalls(self):
        #Goes through each of the keys in the dictionary
        for type in self.walls:
            #Uses the key to access the list associated with each key
            #Goes through each element in the list which is the coordinates
            #of that wall
            for coord in self.walls[type]:
                #Creates a wall object
                wall = objects.Wall(coord, type)
                #Switches one of the empty spots (0) to that wall object
                self.map[coord[1]][coord[0]] = wall
        for wall in self.borderWalls:
            self.walls['empty'].append(wall)

    #Adds the floors to the map
    def addFloors(self):
        #Goes through each type of floor in self.floor dictionary
        for type in self.floors:
            #Uses the key to access coordinates of type of floor
            for coord in self.floors[type]:
                #Creates an object of type floor, passing the coordinates and type
                floor = objects.Floor(coord, type)
                #Changes an empty spot on the map to that object
                self.map[coord[1]][coord[0]] = floor

    #Procedure that adds the door to the map
    def addDoor(self):
        door = objects.Door(self.doorCoord)
        self.map[self.doorCoord[1]][self.doorCoord[0]] = door

    #Function that returns all of the walls or a type of wall
    def getWallCoords(self, category = None):
        allWalls = []
        if category == None:
            for type in self.walls:
                for wall in self.walls[type]:
                    allWalls.append(wall)
            return allWalls
        else:
            return self.walls[category]

    #Function that returns all of the floors or all of a single type of floor
    def getFloorCoords(self, category = None):
        allFloorCoords = []
        if category == None:
            for type in self.floors:
                for floor in self.floors[type]:
                    allFloorCoords.append(floor)
            return allFloorCoords
        else:
            return self.floors[category]

    #Function that returns all of the wall objects
    def getWalls(self, category = None):
        allWalls = []
        coords = self.getWallCoords(category)
        for coord in coords:
            wall = self.map[coord[1]][coord[0]]
            allWalls.append(wall)
        return allWalls

    #Function that returns all of the floor objects
    def getFloors(self, category = None):
        allFloors = []
        coords = self.getFloorCoords(category)
        for coord in coords:
            floor = self.map[coord[1]][coord[0]]
            allFloors.append(floor)
        return allFloors

    #Function that returns an object based on the coordinates
    def getObject(self, coords):
        return self.map[coords[1]][coords[0]]
    
    #Function that returns all of the walls which the player can interact with (walls which have levers etc)
    def getItemWalls(self):
    
        HWalls = self.getWalls('hidingSpace')
        LWalls = self.getWalls('lever')
        interactables = []

        for HWall in HWalls:
            hidingSpace = HWall.getItem()
            interactables.append(HWall)
        for LWall in LWalls:
            lever = LWall.getItem()
            interactables.append(LWall)

        return interactables

    #Function that returns the door object based on the coordinates of the door
    def getDoor(self):
        return self.map[self.doorCoord[1]][self.doorCoord[0]]


                

'''class Node():
    def __init__(self):'''

'''    def getObject(self, type, category = None):
        objects = []
        if type == 'floor':
            coords = self.getWallCoords(category)
        else:
            coords = self.getFloorCoords(category)
        for coord in coords:
            object = self.map[coord[1]][coord[0]]
            objects.append(object)
        return objects'''