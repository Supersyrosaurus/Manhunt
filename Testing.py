import hunter
import pygame
import random
import maps
import mapObjects
pygame.init()

walls = {'empty':mapObjects.empty, 'hidingSpace':mapObjects.hidingSpace, 'lever':mapObjects.lever}
floors = {'wood':mapObjects.wood, 'concrete':mapObjects.concrete, 'carpet':mapObjects.carpet}
doorCoord = mapObjects.doors
map = maps.Map(walls, floors, doorCoord, 20, 30)
map.createMap()

hunterOne = hunter.Hunter(0, 0, 'RedCircle.png', 1, 10, 13)

hunterOne.pathfind((3, 6), map)


















'''proj = False
goalDist = (random.randint(-20, 20), random.randint(-20, 20))


def checkWalls(hunter, goalDist):
    if proj == False:
        print('Created proj')
    dist = hunter.coordinateDistance(goalDist)
    print('dist', dist)
    xDist = dist[0]
    yDist = dist[1]
    direction = hunter.directionCheck(xDist, yDist)
    print('direction', direction)
    angle = hunter.angleCalcR(xDist, yDist)
    print('angle', angle)
    speeds = hunter.speedCalcR(angle)
    xSpeed = speeds[0] * direction[0]
    ySpeed = speeds[1] * direction[1]
    print(xSpeed, ySpeed)

checkWalls(hunterOne, goalDist)'''