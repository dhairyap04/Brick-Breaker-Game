'''
title: window class
author: Dhairya Prajapati
date-created: March 23, 2022
'''
from sprite import Sprite
import pygame


class Window:
    pygame.init()
    def __init__(self):
        title = "Brick Breakout!"
        fps = 30
        width = 800
        height = 600
        lives = 3 
        background = (50,50,150)
        self.TITLE = title
        self.FPS = fps
        self.HEIGHT = height
        self.WIDTH = width
        self.SCREEN_DIMENSIONS = (self.WIDTH, self.HEIGHT)
        self.BACKGROUND = background
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMENSIONS)
        self.SCREEN.fill(self.BACKGROUND)
        self.CAPTION = pygame.display.set_caption(self.TITLE)
        self.KEYS_PRESSED = None

    # --- Modifiers -- #

    def updateScreen(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.SCREEN.fill(self.BACKGROUND)

    def blitSprite(self, sprite):
        self.SCREEN.blit(sprite.getSprite(), sprite.getPOS())

    # -- Accessors -- #
    def getWidth(self):
        return self.SCREEN.get_rect().width

    def getHeight(self):
        return self.SCREEN.get_rect().height
        
    def getKeys(self):
        return self.KEYS_PRESSED

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.KEYS_PRESSED = pygame.key.get_pressed()
