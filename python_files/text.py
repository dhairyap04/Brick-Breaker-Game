'''
title: text class
author: Dhairya Prajapati
date-created: March 23, 2022
'''

from sprite_class import Sprite
import pygame 


class Text(Sprite):

    def __init__(self, value, window, x = 0, y = 0, text = "", font = "Arial" , fontsize = 24, colour = (255, 255, 255)):
        Sprite.__init__(self,window, x, y)
        self.VALUE = value
        self.TEXT = text
        self.PHRASE = text + str(self.VALUE) 
        self.FONT_FAM = font
        self.FONT_SIZE = fontsize
        self.COLOUR = colour
        self.FONT =  pygame.font.SysFont("Arial", 36)
        self.SPRITE = self.FONT.render(self.PHRASE , 1, self.COLOUR)

    # -- Modifiers -- #

    def increaseValue(self):
        self.VALUE += 1
        self.PHRASE = self.TEXT + str(self.VALUE)
        self.SPRITE = self.FONT.render(self.PHRASE, 1, self.COLOUR)

    def decreaseValue(self):
        self.VALUE -= 1
        self.PHRASE = self.TEXT + str(self.VALUE)
        self.SPRITE = self.FONT.render(self.PHRASE, 1, self.COLOUR)

    def setValue(self, value):
        self.VALUE = value
        self.PHRASE = self.TEXT + str(self.VALUE)
        self.SPRITE = self.FONT.render(self.PHRASE, 1, self.COLOUR)
    
    # -- Accessors -- #

    def getValue(self):
        return self.VALUE