#engine.py
'''
title: game class
author: Dhairya Prajapati
date-created: April 12, 2022
'''
# Aggregation is shown in this file

from window import Window
from classes import Block, Ball, Paddle
from text import Text
from sprite_class import Sprite
from pygame import K_SPACE

LIVES = 3

class Game:

    def __init__(self):
        
        self.WINDOW = Window()
        self.BALL = Ball(self.WINDOW, 15)
        self.BALL.setMid()  
        self.PLAYER = Paddle(self.WINDOW, (0 , 0, 0)) 

        self.IN_USE = [] 

        
        self.SCORE = Text(0, self.WINDOW, 2, 10, "Score: ")
        self.LIVES = Text(LIVES, self.WINDOW, text="Lives: ") # Aggregation
        self.LIVES.setPOS(self.WINDOW.getWidth() - self.LIVES.getWidth()-25, 10) 
        self.LEVEL = Text(0, self.WINDOW, 10, self.WINDOW.getHeight() - 40, "Level: ")
        self.START_TEXT = Text("Press Space To Start!", self.WINDOW, self.WINDOW.getWidth() / 2 - 90,300)
        self.STOP = Text("Life Lost! Press Space to Continue", self.WINDOW)
        self.STOP.setPOS(self.WINDOW.getWidth() / 2 - self.STOP.getWidth() - 50, self.WINDOW.getHeight() / 2 - self.STOP.getHeight() / 2)
        self.GAMEOVER = Text("Game Over", self.WINDOW, fontsize=36)
        self.GAMEOVER.setPOS(self.WINDOW.getWidth() / 2 - self.GAMEOVER.getWidth() / 2 - 20 ,self.WINDOW.getHeight() / 2 - self.GAMEOVER.getHeight() / 2)
        self.NEXT_LEVEL = Text("Press Space for next level", self.WINDOW)
        self.NEXT_LEVEL.setPOS(self.WINDOW.getWidth() / 2 - self.NEXT_LEVEL.getWidth() , self.WINDOW.getHeight() - (2 * self.NEXT_LEVEL.getHeight()))
        self.OVER = Text("Press Space to play again", self.WINDOW)
        self.OVER.setPOS(self.WINDOW.getWidth() / 2 - self.OVER.getWidth() / 2 - 100, self.WINDOW.getHeight() - (4 * self.OVER.getHeight() / 2))


        
        self.createBlocks()

        
        self.ARR = [self.BALL, self.PLAYER, self.LEVEL, self.SCORE, self.LIVES, self.START_TEXT]

    # -- Modifier Methods -- #

    def start(self):
        if self.keySpace(self.WINDOW.getKeys()):
            self.ARR.pop()
            self.LEVEL.increaseValue()

    def createBlocks(self):
        for i in range(6):
            for j in range(6):
                TEMP_ARR = [100, 50]
                ARR = TEMP_ARR[i % 2]
                self.IN_USE.append(Block(self.WINDOW, 100, 50))
                self.IN_USE[-1].setPOS(ARR + (j * 105) ,60 + (i * 55))
                self.IN_USE[-1].setColour((255,255,255))

    def run(self):
        halt = False
        max_move = 15
        move = [-1,1]
        next_level = False
        

        while True:

            bounce = 0
            ## Inputs
            self.WINDOW.getEvents()

            ## Processing
            if self.LEVEL.getValue() == 0  and self.LIVES.getValue() != 0: 

                self.start()

            elif self.LEVEL.getValue() != 0 and self.LIVES.getValue() == 0:

                self.ARR = [self.BALL, self.PLAYER, self.LEVEL, self.SCORE, self.LIVES, self.GAMEOVER, self.OVER]

                if self.keySpace(self.WINDOW.getKeys()): 
                    
                    halt = False
                    next_level = False
                    self.resetgame()
                    continue

            elif self.LEVEL.getValue() >= 1 and self.LIVES.getValue() > 0: 

                if halt: 
                    self.ARR = [self.BALL, self.PLAYER, self.LEVEL, self.SCORE, self.LIVES, self.STOP]
                    if self.keySpace(self.WINDOW.getKeys()):
                        self.BALL.restartDirection()
                        self.ARR = [self.BALL, self.PLAYER, self.LEVEL, self.SCORE, self.LIVES]
                        halt = False

                elif next_level:
                    self.PLAYER.setDimensions(100 - (20 * self.LEVEL.getValue()), 10)
                    self.PLAYER.setPOS(self.WINDOW.getWidth() / 2 - self.PLAYER.getWidth() / 2, self.WINDOW.getHeight() - (2 * self.PLAYER.getHeight()))
                    self.ARR = [self.BALL, self.PLAYER, self.LEVEL, self.SCORE, self.LIVES, self.NEXT_LEVEL]
                    if self.keySpace(self.WINDOW.getKeys()):
                        self.BALL.restartDirection()
                        self.ARR.pop()
                        next_level = False
                else:
                    
                    if self.LEVEL.getValue() >= 2:
                        for block in self.IN_USE:
                            block.shakeBlocks(self.LEVEL.getValue(), move[(max_move // 30) % 2])
                        max_move += 1

                    
                    bounce = self.BALL.bounceAround(bounce)
                    if bounce == -1:
                        self.LIVES.decreaseValue()
                        if self.LIVES.getValue() == 0:
                            continue
                        self.BALL.setMid()
                        halt = True
                        continue


                    for block in self.IN_USE:
                        bounce = block.checkCollision(self.BALL)
                        if block.checkHit():
                            self.SCORE.increaseValue()
                            if bounce == 1:
                                self.BALL.bounceHori()
                            elif bounce == 2:
                                self.BALL.bounceVert()

                    for block in self.IN_USE: 
                        if block.checkHit():
                            self.IN_USE.remove(block)

                    if len(self.IN_USE) == 0: 
                        self.LEVEL.increaseValue()
                        self.createBlocks()
                        for block in self.IN_USE:
                            block.hit = False
                            self.BALL.setMid()
                        next_level = True
                        continue

                    self.PLAYER.move(self.WINDOW.getKeys())

                    if 1 == self.PLAYER.checkCollision(self.BALL): 
                        self.BALL.bounceVert()
                    elif 2 == self.PLAYER.checkCollision(self.BALL): 
                        self.BALL.bounceHori()


            # Outputs

            self.WINDOW.clearScreen()

            if self.LEVEL.getValue() >= 1 and self.LIVES.getValue() > 0 and not halt:
                for block in self.IN_USE:
                    self.WINDOW.blitSprite(block)

            for item in self.ARR:
                self.WINDOW.blitSprite(item)

            self.WINDOW.updateScreen()

    def resetgame(self):
        self.ARR = [self.BALL, self.PLAYER,  self.LEVEL, self.SCORE, self.LIVES]
        self.IN_USE = []
        self.createBlocks()
        self.BALL.setMid()
        self.PLAYER.setPOS(self.WINDOW.getWidth() / 2 - self.PLAYER.getWidth() / 2,self.WINDOW.getHeight() - (2 * self.PLAYER.HEIGHT))
        self.LEVEL.setValue(1)
        self.SCORE.setValue(0)
        self.LIVES.setValue(3)


    # -- Accessor Methods -- #

    def keySpace(self,keys):
        if keys[K_SPACE] == 1:
            return True
