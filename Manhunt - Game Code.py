import pygame

#Initialising the pygame module
pygame.init()

keepScreen = True

while keepScreen == True:
    #Creating a screen
    screen = pygame.display.set_mode((800,600))
    input = int(input('Keep screen?'))
    if input == 1:
        keepScreen = False
