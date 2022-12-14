import pygame
import screens
import objects

#Initialising the pygame module
pygame.init()

wall1 = objects.Wall(240, 140, 200, 200)

wall2 = objects.Wall(250, 150, 200, 200, 0)

wall3 = objects.Wall(250, 150, 200, 200, 1)

door = objects.Door(100, 150, 100, 50)

carpet = objects.Floor(300, 500, 200, 200, 0)

concrete =  objects.Floor(300, 400, 100, 100, 1)

wood = objects.Floor(200, 300, 50, 50, 2)

print('WALL')

print(str(wall1.wall))
print(str(wall2.wall))
print(str(wall3.wall))

print(str(wall1.getCoords()))
print(str(wall2.getCoords()))

print(str(wall3.wall.checkLeverActivation()))
wall3.wall.activate()
print(str(wall3.wall.checkLeverActivation()))
wall3.wall.deactivate()
print(str(wall3.wall.checkLeverActivation()))

print('DOOR')

print(str(door.checkDoorActivation()))
door.isActivated(3, 5)
print(str(door.checkDoorActivation()))
door.isActivated(5, 5)
print(str(door.checkDoorActivation()))

print('FLOOR')

print('CARPET')
print(str(carpet.checkSoundLevel()))
print('CONCRETE')
print(str(concrete.checkSoundLevel()))
print('WOOD')
print(str(wood.checkSoundLevel()))