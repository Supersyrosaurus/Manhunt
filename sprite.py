import pygame

pygame.init()

class Sprite():
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

    #This method moves the player up by a specific number of pixels in the negative Y direction
    def moveForward(self):
        self.resetMovement()
        self.forward = True
        if self.sprinting == True:
            self.y -= self.speed * self.sprintMultiplier
        else:
            self.y -= self.speed
    
    #This method moves the player up by a specific number of pixels in the positive Y direction
    def moveBackward(self):
        self.resetMovement()
        self.backward = True
        if self.sprinting == True:
            self.y += self.speed * self.sprintMultiplier
        else:
            self.y += self.speed

    #This method moves the player up by a specific number of pixels in the negative X direction
    def moveLeft(self):
        self.resetMovement()
        self.left = True
        if self.sprinting == True:
            self.x -= self.speed * self.sprintMultiplier
        else:
            self.x -= self.speed

    #This method moves the player up by a specific number of pixels in the positive X direction
    def moveRight(self):
        self.resetMovement()
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
        collisionTolerance = 3
        #This loop goes through each wall in the list above
        for wall in walls:
            #Gets the rectangle of the wall
            wallRect = wall.getRect()
            spriteRect = self.hitbox
            #Checks if the rectangle of the player has collided with that rectangle (for the wall)
            if spriteRect.colliderect(wallRect):
                #Each of these if statements check which direction the player is currently moving
                #and based on this decision, the direction the player bounces back is determined
                if self.backward == True or abs(spriteRect.bottom - wallRect.top) <= collisionTolerance:
                    self.y -= collisionBounce

                if self.forward == True or abs(spriteRect.top - wallRect.bottom) <= collisionTolerance:
                    self.y += collisionBounce


                if self.right == True or abs(spriteRect.right - wallRect.left) <= collisionTolerance:
                    self.x -= collisionBounce

                if self.left == True or abs(spriteRect.left - wallRect.right) <= collisionTolerance:
                    self.x += collisionBounce

    def getHitbox(self):
        return self.hitbox

    def displaySprite(self, screen):
        screen.blit(self.transformedImg, self.hitbox.topleft)
    
    def resetMovement(self):
        self.forward = False
        self.left = False
        self.right = False
        self.backward = False