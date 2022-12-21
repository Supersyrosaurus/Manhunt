import pygame
import screens
import objects
import maps

#Initialising the pygame module
pygame.init()

wallsDic = {'empty':[1,2,3], 'hidingSpace':[4,5,6], 'lever':[7,8,9]}
floorsDic = {'wood':[], 'concrete':[], 'carpet':[]}
doorCoord = (1, 3)

print(wallsDic)
for list in wallsDic:
    print(wallsDic[list])
    for element in wallsDic[list]:
        print(element)

gameMap = maps.Map(wallsDic, floorsDic, doorCoord, 5)
'''gameMap.addHeight()
print(gameMap.map)'''




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




