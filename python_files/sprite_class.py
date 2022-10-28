#sprite_class.py
'''
title: abstract class for sprites
author: Dhairya Prajapati
date-created: April 22, 2022
'''

from pygame import Surface, SRCALPHA

class Sprite:

    def __init__(self, window, x = 0, y = 0, colour = (255,255,255)): 
        self.WIDTH = 100
        self.HEIGHT = 100
        self.DIMENSIONS = (self.WIDTH, self.HEIGHT)
        self.SPRITE = Surface(self.DIMENSIONS,SRCALPHA, 32)
        self.COLOUR = colour
        self.SPRITE.fill(self.COLOUR)
        self.X = x
        self.Y = y
        self.POS = (self.X, self.Y)
        self.WINDOW = window

    # -- Modify Methods -- #

    def updateSprite(self):
        self.DIMENSIONS = (self.WIDTH, self.HEIGHT)
        self.SPRITE = Surface(self.DIMENSIONS, SRCALPHA, 32)
        self.SPRITE.fill(self.COLOUR) 

    def setWidth(self, width):
        self.WIDTH = width
        self.updateSprite()

    def setHeight(self, height):
        self.HEIGHT = height
        self.updateSprite()

    def setColour(self, colour):
        self.COLOUR = colour
        self.updateSprite()

    def setDimensions(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.updateSprite()

    def setX(self, x):
        self.X = x
        self.POS = (self.X, self.Y)

    def setY(self, y):
        self.Y = y
        self.POS = (self.X, self.Y)

    def setPOS(self, x, y):
        self.X = x
        self.Y = y
        self.POS = (self.X, self.Y)

    # -- Accessor Methods -- #

    def getSprite(self):
        return self.SPRITE

    def getRect(self): 
        return self.SPRITE.get_rect(x = self.X, y = self.Y)

    def getPOS(self):
        return self.POS

    def getWidth(self):
        return self.WIDTH

    def getHeight(self):
        return self.HEIGHT

    def getX(self):
        return self.X

    def getY(self):
        return self.Y