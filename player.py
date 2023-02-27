import pygame
import maps
import objects
import physics
import time
pygame.init()

class Player(pygame.sprite.Sprite, physics.Projectile):
    def __init__(self, x, y, img, scale, speed, sprintMultiplier, map):
        super().__init__
        #Coordinate attributes
        self.x = x
        self.y = y
        self.mapCoords = self.setMapCoords()
        #Image attributes
        self.img = pygame.image.load(img).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height()
        self.transformedImg = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))
        self.width = self.transformedImg.get_width()
        self.height = self.transformedImg.get_height()
        #Hitbox of the player by creating a rectangle around the player img
        self.hitbox = self.transformedImg.get_rect()
        #Activation area for the player to use to detect levers and hiding places around the player when the player interacts
        self.activationArea = pygame.Rect(self.x - 32, self.y - 32, self.width * 3, self.height * 3)
        #Speed in any direction
        self.speed = speed
        #This is the sprinting multiplier which increases the speed of the player by that much
        self.sprintMultiplier = sprintMultiplier
        #This is the current state of whether the player is hiding or not
        self.hiding = False
        self.sound = self.setSound(map)
        #These are the attributes for the levers
        self.maxLevers = None
        self.activatedLevers = 0
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False

    #Displays the player on whatever screen is passed to the method
    def displayPlayer(self, screen):
        if self.getHiding() == False:
            pygame.draw.rect(screen, (255, 255, 255), self.activationArea)
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox)
            screen.blit(self.transformedImg, self.hitbox.topleft)
        

    #Checks if the W key has been pressed and if it has then it deducts 1 from the player coordinates and update
    #the coordinates of the player
    def moveForward(self, pressed, sprintCheck):
        if pressed[pygame.K_w] and sprintCheck:
            self.y -= self.speed * self.sprintMultiplier
            self.setMovement(True, 'F')
        elif pressed[pygame.K_w]:
            self.y -= self.speed
            self.setMovement(True, 'F')
        else:
            self.setMovement(False, 'F')
        self.setCoords()            

    #Checks if the S key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def moveBackward(self, pressed, sprintCheck):
        if pressed[pygame.K_s] and sprintCheck:
            self.y += self.speed * self.sprintMultiplier
            self.setMovement(True, 'B')
        elif pressed[pygame.K_s]:
            self.y += self.speed
            self.setMovement(True, 'B')
        else:
            self.setMovement(False, 'B')
        self.setCoords()            

    #Checks if the D key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def moveRight(self, pressed, sprintCheck):
        if pressed[pygame.K_d] and sprintCheck:
            self.x += self.speed * self.sprintMultiplier
            self.setMovement(True, 'R')
        elif pressed[pygame.K_d]:
            self.x += self.speed
            self.setMovement(True, 'R')
        else:
            self.setMovement(False, 'R')
        self.setCoords()

    #Checks if the A key has been pressed and if it has then it deducts 1 from the players coordinates and updates 
    #the coordintes of the player
    def moveLeft(self, pressed, sprintCheck):
        if pressed[pygame.K_a] and sprintCheck:
            self.x -= self.speed * self.sprintMultiplier
            self.setMovement(True, 'L')
        elif pressed[pygame.K_a]:
            self.x -= self.speed  
            self.setMovement(True, 'L')
        else:
            self.setMovement(False, 'L')
        self.setCoords()


    def leverCheck(self, item, map):
        #Checks if the item is a lever
        if isinstance(item, objects.Lever):
            #Checks if the lever has already been activated
            if item.getActivated() == False:
                self.activateLever()
                #Activates that specific lever so it cannot be activated again
                item.activate()
                print('activated lever')

            else:
                print('LEVER HAS ALREADY BEEN ACTIVATED')

    #This procedure checks if the object is a hiding space
    def hideCheck(self, item):
        #Checks if the item is a hidingspace
        if isinstance(item, objects.HidingSpace):
            self.setHiding(True)
            print('Hiding Space')

    #This procedure carries out the interaction function for the player 
    def interact(self, pressed, map):
        if pressed[pygame.K_e]:
            if self.hiding == False:
                #Uses a function which returns a list of the walls with items and gives it an identifier
                itemWalls = map.getItemWalls()
                #Goes through each one of these walls
                for itemWall in itemWalls:
 
                    #Checks if the player's activation area has collided with the wall with an item, 
                    #If the player's activation area has collided with the wall, they are close enough
                    if self.activationArea.colliderect(itemWall.getRect()):
                        #item is the wall which also contains either a hiding space or lever
                        item = itemWall.getItem()
                        self.hideCheck(item)
                        self.leverCheck(item, map)
                    
            else:
                self.setHiding(False)


    #This returns a boolean value based on if the player is pressing the shift button or not
    def sprintCheck(self, pressed):
        if pressed[pygame.K_LSHIFT]:
            return True
        else: 
            return False

    #This changes the coordinates of the player whenever it is called, as the map coordinates of the player are directly linked to the 
    #screen coordinates of the player, by changing the screen coordinates (which moves the player image and rect) it also changes the
    #players location on the other map
    def setCoords(self):
        self.hitbox.center = (self.x, self.y)
        #Sets the coordinates of the activation area as the center of the hitbox of the player
        self.activationArea.center = self.hitbox.center
    
    def setMapCoords(self):
        x = round(self.x/32)
        y = round(self.y/32)
        return (x, y)

    #This returns the coordinates of the player divided by 32 as the size of the map is a factor of 32 compared to the size of the screen
    def getMapCoords(self):
        return self.mapCoords

    #This returns the center of the hitbox which is in the same place as the player
    def getCoords(self):
        return self.hitbox.center

    #This method checks if the W, A, S, D, E, or LEFT SHIFT buttons are pressed and then carries out various actions depending 
    #on the button that is pressed 
    def checkKeys(self, map):
        #Uses a pygame method to check if any key has been pressed and will be true if it is pressed and false if no buttons
        #on the keyboard are being pressed
        pressed = pygame.key.get_pressed()
        hiding = self.getHiding()
        sprintCheck = self.sprintCheck(pressed)
        self.checkWin(map)

        #Each of these methods control an aspect of the inputs from the user which in turn controls the player
        if hiding == False:
            self.moveForward(pressed, sprintCheck)
            self.moveBackward(pressed, sprintCheck)
            self.moveRight(pressed, sprintCheck)
            self.moveLeft(pressed, sprintCheck)
        self.interact(pressed, map)

    #This sets the sound that the player is making based on the coordinates of the player on the map
    def setSound(self, map):
        coords = self.getMapCoords()
        floor = map.getObject(coords)
        if isinstance(floor, objects.Floor):
            return floor.getSoundLevel()
        else:
            print('NOT FLOOR')

    #This returns the sound level for the player
    def getSound(self):
        return self.sound
    
    #This returns the value for the number of activated levers
    def getActivatedLevers(self):
        return self.activatedLevers
    
    #This function adds 1 to the number of activated levers if not all of the levers have been activated
    def activateLever(self):
        self.activatedLevers += 1
        print(self.activatedLevers)

    #This returns the max number of levers that are in the game 
    def getMaxLevers(self):
        return self.maxLevers

    #This returns a boolean value of the attribute for if the player is hiding or not
    def getHiding(self):
        return self.hiding
    
    #This sets the value of hiding pabased on the parameter that is passed which has to be a boolean value
    def setHiding(self, hiding):
        if hiding == True or hiding == False:    
            self.hiding = hiding
        else:
            print('HIDING IS NOT BOOLEAN VALUE')

    #This procedure gets a list of all of the levers from the map class and then sets the number of max levers as the length of that list
    def setMaxLevers(self, map):
        levers = map.getWalls('lever')
        self.maxLevers = len(levers)

    #This function sets the movement directions as a boolean value based on the parameters passed
    def setMovement(self, value, direction = None):
        #Validates that the value passed is a boolean value
        if value != True and value != False:
            print('THIS VALUE IS INVALID, MUST BE BOOLEAN')
        #If data is validated then attribute can be modified based on the direction passed
        else:
            #Each value can be changed based on the direction, however, 2 cannot be changed at the same time
            #in this function
            if direction != None:
                if direction == 'F':
                    self.forward = value
                elif direction == 'B': 
                    self.backward = value
                elif direction == 'L':
                    self.left = value
                elif direction == 'R':
                    self.right = value
            else:
                self.forward = value
                self.backward = value
                self.left = value
                self.right = value

    #This function checks if the player has activated all of the levers and then returns a boolean value based on that
    def checkWin(self, map):
        #function returns the door objects in a list
        doors = map.getDoor()
        print(self.getActivatedLevers())
        print(self.getMaxLevers())
        #checks if the player has activated all of the levers
        if self.getActivatedLevers() == self.getMaxLevers():
            #As there are multiple doors, this loop goes through each door 
            for door in doors:
                door.activate()
                #Checks if each door has been collided with and carries out action based on that
                if self.hitbox.colliderect(door.getRect()):
                    print('WIN')

    #This is the function which checks for collisions of the player with walls and then causes the player to bounce off of it
    def checkCollision(self, map):
        #This function returns all of the walls for the map in a list
        walls = map.getWalls()
        collisionTolerance = 15
        #This is how many pixels the player will bounce off the wall when collision occurs
        collisionBounce = 10
        player = self.hitbox
        #This loop goes through each wall in the list above
        for wall in walls:
            #Gets the rectangle of the wall
            rect = wall.getRect()
            'print(str(player.colliderect(rect)))'
            #Checks if the rectangle of the player has collided with that rectangle (for the wall)
            if self.hitbox.colliderect(rect):
                print('COLLIDING')
                #Each of these if statements check which direction the player is currently moving
                #and based on this decision, the direction the player bounces back is determined
                if self.backward == True:
                    print('BOTTOM')
                    self.y -= collisionBounce

                if self.forward == True:
                    print('TOP')
                    self.y += collisionBounce


                if self.right == True:
                    print('RIGHT')
                    self.x -= collisionBounce

                if self.left == True:
                    print('LEFT')
                    self.x += collisionBounce
                

#FOR SIGHT USE COLLIDE RECT AND EVERY FLOOR TILE COLLIDED WITH MAKE COLOURED BUT ONLY MAKE WALL COLOURED WHEN COLLIDE


###########################     UNUSED CODE     ####################################


                
'''if self.getActivatedLevers() == self.getMaxLevers():
    door = map.getDoor()
    door.activate()
    print('ALL LEVERS HAVE BEEN ACTIVATED')   ''' 

'''if abs(rect.top - player.bottom) < collisionTolerance and self.backward == True:
    print('BOTTOM')
    self.y -= collisionBounce

if abs(rect.bottom - player.top) < collisionTolerance and self.forward == True:
    print('TOP')
    self.y += collisionBounce


if abs(rect.left - player.right) < collisionTolerance and self.right == True:
    print('RIGHT')
    self.x -= collisionBounce

if abs(rect.right - player.left) < collisionTolerance and self.left == True:
    print('LEFT')
    self.x += collisionBounce'''

'''    def playerToWallDistance(self,wallCoords):
        playerCoords = self.getCoords()
        #Sets x and y coordinates of the player as variables
        xP = playerCoords[0]
        yP = playerCoords[1]
        xW = wallCoords[0]
        yW = wallCoords[1]
        xdist = abs(xP - xW)
        ydist = abs(yP - yW)
        #Calculates distance of player and wall from origin using method from physics class
        distance = self.pythagoras(xdist, ydist)
        #print(playerDistance)
        #print(wallDistance)
        return distance'''