import pygame
import maps
import objects
import physics
import time
import sprite
pygame.init()

    
class Player(sprite.Sprite):
    def __init__(self, x, y, img, scale, speed, sprintMultiplier, map):
        super().__init__(x, y, img, scale, speed, sprintMultiplier)
        #Activation area for the player to use to detect levers and hiding places around the player when the player interacts
        self.activationArea = pygame.Rect(self.x - 32, self.y - 32, self.width * 3, self.height * 3)
        self.hiding = False
        self.sound = None
        #These are the attributes for the levers
        self.maxLevers = None
        self.activatedLevers = 0
        self.sightProjectiles = []
        self.collided = []
        self.sound = None
        self.sprintTimer = 0
        self.interacted = False


    #Displays the player on whatever screen is passed to the method
    def displayPlayer(self, screen):
        if self.getHiding() == False:
            self.displaySprite(screen)

    #Checks if the W key has been pressed and if it has then it deducts 1 from the player coordinates and update
    #the coordinates of the player
    def checkForward(self, pressed):
        if pressed[pygame.K_w]:
            self.moveForward()
        else:
            self.forward = False
        self.setPlayerCoords()            

    #Checks if the S key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def checkBackward(self, pressed):
        if pressed[pygame.K_s]:
            self.moveBackward()
        else:
            self.backward = False
        self.setPlayerCoords()            

    #Checks if the D key has been pressed and if it has then it increments the players coordinates by 1 and updates
    #the coordinates of the player
    def checkRight(self, pressed):
        if pressed[pygame.K_d]:
            self.moveRight()
        else:
            self.right = False
        self.setPlayerCoords()

    #Checks if the A key has been pressed and if it has then it deducts 1 from the players coordinates and updates 
    #the coordintes of the player
    def checkLeft(self, pressed):
        if pressed[pygame.K_a]:
            self.moveLeft() 
        else:
            self.left = False
        self.setPlayerCoords()


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

    def interactCheck(self, event, map):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                self.interact(map)
        
        
    #This procedure carries out the interaction function for the player 
    def interact(self,map):
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
            self.setSprinting(True)
        else: 
            self.setSprinting(False)

    #This changes the coordinates of the player whenever it is called, as the map coordinates of the player are directly linked to the 
    #screen coordinates of the player, by changing the screen coordinates (which moves the player image and rect) it also changes the
    #players location on the other map
    def setPlayerCoords(self):
        self.setCoords()
        #Sets the coordinates of the activation area as the center of the hitbox of the player
        self.activationArea.center = self.hitbox.center


    #This method checks if the W, A, S, D, E, or LEFT SHIFT buttons are pressed and then carries out various actions depending 
    #on the button that is pressed 
    def checkKeys(self, map):
        #Uses a pygame method to check if any key has been pressed and will be true if it is pressed and false if no buttons
        #on the keyboard are being pressed
        pressed = pygame.key.get_pressed()
        hiding = self.getHiding()
        self.sprintCheck(pressed)
        win = self.checkWin(map)

        #Each of these methods control an aspect of the inputs from the user which in turn controls the player
        if hiding == False:
            self.checkForward(pressed)
            self.checkBackward(pressed)
            self.checkRight(pressed)
            self.checkLeft(pressed)
        return win
        

    def checkSound(self, map):
        coords = self.getMapCoords()
        floor = map.getObject(coords)
        if isinstance(floor, objects.Floor):
            sound = floor.getSoundLevel()
            self.setSound(sound)
        else:
            print('NOT FLOOR')

    #This sets the sound that the player is making based on the coordinates of the player on the map
    def setSound(self, value):
        if value <= 0 or value >= 1:
            print('INCORRECT VALUE')
            return
        self.sound = value
        

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

    #This function checks if the player has activated all of the levers and then returns a boolean value based on that
    def checkWin(self, map):
        #function returns the door objects in a list
        doors = map.getDoors()
        #print(self.getActivatedLevers())
       # print(self.getMaxLevers())
        #checks if the player has activated all of the levers
        if self.getActivatedLevers() == self.getMaxLevers():
            #As there are multiple doors, this loop goes through each door 
            for door in doors:
                door.activate()
                #Checks if each door has been collided with and carries out action based on that
                if self.hitbox.colliderect(door.getRect()):
                    #Returns to end game loop
                    return True

                
    #This creates the projectiles around the player which will be used for the field of view
    def createProjectiles(self):
        #This is the length of each side of the projectile in pixels which will be passed into the projectiles class
        length = 32

        #As there was no simpler way to create a loop as the projectiles need a specific speed, each one had to be created individually
        projectile1 = physics.SightProjectile(self.getHitbox().topleft, 0, 5, length)
        projectile2 = physics.SightProjectile(self.getHitbox().topleft, 0, -5, length)
        projectile3 = physics.SightProjectile(self.getHitbox().topleft, 5, 0, length)
        projectile4 = physics.SightProjectile(self.getHitbox().topleft, -5, 0, length)
        projectile5 = physics.SightProjectile(self.getHitbox().topleft, -5, -5, length)
        projectile6 = physics.SightProjectile(self.getHitbox().topleft, -5, 5, length)
        projectile7 = physics.SightProjectile(self.getHitbox().topleft, 5, 5, length)
        projectile8 = physics.SightProjectile(self.getHitbox().topleft, 5, -5, length)

        #As the projectiles were created as individual variables, they must be appended to the projectiles list individually as well
        self.sightProjectiles.append(projectile1)
        self.sightProjectiles.append(projectile2)
        self.sightProjectiles.append(projectile3)
        self.sightProjectiles.append(projectile4)
        self.sightProjectiles.append(projectile5)
        self.sightProjectiles.append(projectile6)
        self.sightProjectiles.append(projectile7)
        self.sightProjectiles.append(projectile8)


    def fov(self, map, screen):
        #This variable holds a 1D list of all of the objects in the map
        allObjects = map.getAllObjects()
        #This for loop goes through each of the objects in the list aboce
        for object in allObjects:
            #This sets the visibility of each object as False so that it appears black on the screen
            object.setVisible(False)
    
        #This checks if the projectiles have been made yet as they are appended to the list straight after they are made
        #and the projectiles only need to be created once as they can be launched many times
        if len(self.sightProjectiles) == 0:
            self.createProjectiles()

        #This for loop goes through each projectile in the self.projectiles list
        for projectile in self.sightProjectiles:
            #This if statement checks whether the projectile has yet to be launched for the first time or if it has collided with the wall and finished
            if projectile.getCollided() == True or projectile.getLaunched() == False:
                #If either of the above is true then it sets the collided attribute of the projectile as false
                projectile.setCollided(False)
                #and then re-launches the projectile again to check, a list of objects it has collided with are returned
                collided = projectile.launchSightProjectile(screen, map, self.getHitbox().center)
                #This list is then appended to the self.collided list
                self.collided.append(collided)

        #This nested for loop goes through each object that all the projectiles have collided with
        for projectile in self.collided:
            for object in projectile:
                #This sets the visibility of the object as true so that the player can see it
                object.setVisible(True)
        #The self.collided list has to be reset each time otherwise the previous objects would also be set as visible to the player
        self.collided = []

    def getCollided(self):
        return self.collided
    
    def ready(self, map, screen):
        self.displayPlayer(screen.getScreen())
        self.fov(map, screen)
        self.checkCollision(map)
        self.checkSound(map)
        win = self.checkKeys(map)
        if win:
            return True
        

###########################     UNUSED CODE     ####################################
'''class Sprite():
    def __init__(self, x, y, img, scale, speed, sprintMultiplier):
        self.x = x
        self.y = y
        self.mapX = round(self.x/32)
        self.mapY = round(self.y/32) 
        #Image attributes
        self.img = pygame.image.load(img).convert_alpha()
        width = self.img.get_width()
        height = self.img.get_height()
        self.transformedImg = pygame.transform.scale(self.img, (int(width * scale), int(height * scale)))
        self.width = self.transformedImg.get_width()
        self.height = self.transformedImg.get_height()
        #Hitbox of the player by creating a rectangle around the player img
        self.hitbox = self.transformedImg.get_rect()
        #Speed in any direction
        self.speed = speed
        #This is the sprinting multiplier which increases the speed of the player by that much
        self.sprintMultiplier = sprintMultiplier
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False
        self.sprinting = False

    def moveForward(self):
        self.forward = True
        if self.sprinting == True:
            self.y -= self.speed * self.sprintMultiplier
        else:
            self.y -= self.speed
    
    def moveBackward(self):
        self.backward = True
        if self.sprinting == True:
            self.y += self.speed * self.sprintMultiplier
        else:
            self.y += self.speed

    def moveLeft(self):
        self.left = True
        if self.sprinting == True:
            self.x -= self.speed * self.sprintMultiplier
        else:
            self.x -= self.speed


    def moveRight(self):
        self.right = True
        if self.sprinting == True:
            self.x += self.speed * self.sprintMultiplier
        else:
            self.x += self.speed

    def setSprinting(self, value):
        if value == True or value == False:
            self.sprinting = value
        else:
            print('NOT RIGHT DATA TYPE FOR SPRINTING')
            
        
    def getSprinting(self):
        return self.sprinting
    
    def getForward(self):
        return self.forward

    def getBackward(self):
        return self.backward

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


    def setCoords(self):
        self.hitbox.center = (self.x, self.y)

    #This returns the coordinates of the player divided by 32 as the size of the map is a factor of 32 compared to the size of the screen
    def getMapCoords(self):
        x = round(self.hitbox.center[0]/32)
        y = round(self.hitbox.center[1]/32)
        return (x, y)

    #This returns the center of the hitbox which is in the same place as the player
    def getCoords(self):
        return self.hitbox.center

    #This is the function which checks for collisions of the player with walls and then causes the player to bounce off of it
    def checkCollision(self, map):
        #This function returns all of the walls for the map in a list
        walls = map.getWalls()
        #This is how many pixels the player will bounce off the wall when collision occurs
        collisionBounce = 5
        #This loop goes through each wall in the list above
        for wall in walls:
            #Gets the rectangle of the wall
            rect = wall.getRect()
            'print(str(player.colliderect(rect)))'
            #Checks if the rectangle of the player has collided with that rectangle (for the wall)
            if self.hitbox.colliderect(rect):
                #print('COLLIDING')
                #Each of these if statements check which direction the player is currently moving
                #and based on this decision, the direction the player bounces back is determined
                if self.backward == True:
                    #print('BOTTOM')
                    self.y -= collisionBounce

                if self.forward == True:
                    #print('TOP')
                    self.y += collisionBounce


                if self.right == True:
                   # print('RIGHT')
                    self.x -= collisionBounce

                if self.left == True:
                    #print('LEFT')
                    self.x += collisionBounce

    def getHitbox(self):
        return self.hitbox

    def displaySprite(self, screen):
        screen.blit(self.transformedImg, self.hitbox.topleft)
'''