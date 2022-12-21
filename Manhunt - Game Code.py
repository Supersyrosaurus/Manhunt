import pygame
import screens
import objects
import maps

#Initialising the pygame module
pygame.init()

wallsDic = {'empty':[(1,1), (1, 2), (1, 3)], 'hidingSpace':[(2,1),(2,2),(2,3)], 'lever':[(3,1), (3,2), (3,3)]}
floorsDic = {'wood':[(1,4),(2,4),(3,4),(4,4),(5,4)], 'concrete':[(1,5),(2,5),(3,5),(4,5),(5,5)], 'carpet':[(4,1),(4,2),(4,3)]}
doorCoord = (6, 3)

gameMap = maps.Map(wallsDic, floorsDic, doorCoord, 5)
gameMap.createEmptyMap()
gameMap.addWalls()
gameMap.addFloors()
gameMap.addDoor()
for y in gameMap.map:
    print(y)



#Loop for game screen
'''running = True'''
'''while running:

    #Changing background colour
    mainMenu.displayScreen()
    if mainMenu.searchButton('start').clickCheck(mainMenu.screen) == True:
        print('Start')
    if mainMenu.searchButton('options').clickCheck(mainMenu.screen) == True:
        mainMenu.closeScreen()
        settings.displayScreen()
        print('Setting')


    #event handler
    for event in pygame.event.get():
        #Checks through all of the events that are happening in the window
        #If user presses cross button window closed
        if event.type == pygame.QUIT:
            running = False'''
        
'''        if settings.searchButton('start').clickCheck(mainMenu.screen) == True:
            print('Start')
        if settings.searchButton('options').clickCheck(mainMenu.screen) == True:
            settings()
            print('settings')
            running = False'''

#Going through a dictionary
'''print(wallsDic)
for list in wallsDic:
    print(wallsDic[list])
    for element in wallsDic[list]:
        print(element)'''


