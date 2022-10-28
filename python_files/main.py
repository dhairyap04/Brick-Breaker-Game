'''
title: main file to run code
author: Dhairya Prajapati
date-created: April 27, 2022
'''

from game import Game
import pygame

if __name__ == "__main__":
    pygame.init()
    game =  Game()
    game.run()