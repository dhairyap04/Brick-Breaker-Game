#classes.py
'''
title: Block, Ball, and Paddle Classes
author: Dhairya Prajapati
date-created: April 20, 2022
'''
# Inheritance, Encapsulation, and Polymorphism are shown in this file. 
# Polymorphism because checkCollision functions are different in Block class and Paddle Class

from window import Window
from sprite import Sprite
from pygame import K_d, K_a
from random import randrange

class Block(Sprite): # Inheritance from Sprite class
    def __init__(self, window, width, height):
        Sprite.__init__(self, window)
        self.setDimensions(width, height)
        self.__HIT = False 

    # -- Modifier Methods -- #
    def shakeBlocks(self, level, direction): 
        if level > 1:
            self.setPOS(self.getX() + (direction * 2), self.getY() + (direction * 2))

    def getHit(self):
        self.__HIT = True ## Encapsulation as it is a private variable ##

    # -- Accessor Methods -- #

    def checkCollision(self, ball): 

        # Collisions
        if self.getRect().colliderect(ball.getRect()): 
            self.getHit() 
            
            top_left = (ball.getX(), ball.getY())  
            top_right = (ball.getX() + ball.getWidth(), ball.getY())
            bottom_right = (ball.getX() + ball.getWidth(), ball.getY() + ball.getHeight())
            bottom_left = (ball.getX(), ball.getY() + ball.getHeight())
            

            if top_left[0] >= (self.getX() + self.getWidth() - ball.SPEED) and bottom_left[0] >= (self.getX() + self.getWidth() - ball.SPEED) and top_left[1] <= (self.getY()+ self.getHeight()+ball.SPEED) and bottom_left[1] >= (self.getY() - ball.SPEED): 
                return 1 
            elif top_right[0] <= (self.getX()+ball.SPEED) and bottom_right[0] <= (self.getX()+ball.SPEED) and top_right[1] <= (self.getY()+ self.getHeight()+ball.SPEED) and bottom_right[1] >= (self.getY() - ball.SPEED):
                return 1 
            else:
                return 2 

    def checkHit(self):
        return self.__HIT


class Ball(Sprite): # Inheritance from Sprite class

    def __init__(self, window, size):
        Sprite.__init__(self, window)
        self.setDimensions(size, size)
        self.DIRX = randrange(-1, 2, 2)
        self.DIRY = -1
        self.SPEED = 5

    # -- Modifier Methods -- #

    def bounceAround(self, bounce): 
        self.X += self.SPEED * self.DIRX
        self.Y += self.SPEED * self.DIRY

        if self.X > self.WINDOW.getWidth() - self.WIDTH:
            self.X = self.WINDOW.getWidth() - self.WIDTH
            self.DIRX = -1
        elif self.X < 0:
            self.X = 0
            self.DIRX = 1
        #
        if self.Y >= self.WINDOW.getHeight() - self.HEIGHT:
            self.Y = self.WINDOW.getHeight() - self.HEIGHT
            self.DIRY = -1
            return -1 

        elif self.Y < 0:
            self.Y = 0
            self.DIRY = 1
        #
        self.POS = (self.X, self.Y)
        return bounce 

    def bounceHori(self):
        self.DIRX *= -1

    def bounceVert(self):
        self.DIRY *= -1

    def bounceBoth(self): 
        self.bounceVert()
        self.bounceHori()

    def setMid(self): 
        self.setPOS(self.WINDOW.getWidth() / 2 - self.getWidth() / 2 , randrange(530, 561, 1))

    def restartDirection(self): 
        self.DIRX = randrange(-1, 2, 2) 
        self.DIRY = -1


class Paddle(Sprite): # Inheritance from Sprite class
    def __init__(self, window, colour):
        Sprite.__init__(self, window, colour=colour)
        self.SPEED = 10
        self.setDimensions(100, 10)
        self.setPOS(self.WINDOW.getWidth() / 2 - self.getWidth() / 2, self.WINDOW.getHeight() - (2 * self.HEIGHT))

    # -- Modifier Methods -- #

    def move(self, keys):

        if keys[K_d] == 1:
            self.X += self.SPEED
        if keys[K_a] == 1:
            self.X -= self.SPEED

        # check boundaries apart of this function

        if self.X > self.WINDOW.getWidth() - self.SPRITE.get_rect().width:
            self.X = self.WINDOW.getWidth() - self.SPRITE.get_rect().width
        elif self.X < 0:
            self.X = 0

        self.POS = (self.X, self.Y)

    # -- Accessor Methods -- #

    def checkCollision(self, ball):
        if self.SPRITE.get_rect(x = self.X, y = self.Y).colliderect(ball.getSprite().get_rect(x = ball.getX(), y = ball.getY())): 
            
            bottom_right = (ball.getX() + ball.getWidth(), ball.getY() + ball.getHeight())
            bottom_left = (ball.getX(), ball.getY() + ball.getHeight())
            
            if bottom_left[0] <= (self.getX() + self.getWidth()) and bottom_right[0] >= self.getX() and bottom_left[1] <= self.getY() + ball.SPEED: 
                return 1 
            else:
                return 2 
        else:
            return 0 
