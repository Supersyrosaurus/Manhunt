import pygame
import screens
import objects

#Initialising the pygame module
pygame.init()

wall1 = objects.Wall(240, 140, 200, 200)

wall2 = objects.Wall(250, 150, 200, 200, 0)

wall3 = objects.Wall(250, 150, 200, 200, 1)

print(str(wall1.wall))
print(str(wall2.wall))
print(str(wall3.wall))

print(str(wall1.getCoords()))
print(str(wall2.getCoords()))

