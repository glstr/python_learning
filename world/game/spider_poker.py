#!/usr/bin/python
# coding=utf-8

import sys
import pygame 
from pygame.locals import * 

default_size = (1080, 720)
background_img_path = "data/background.jpeg"

poker_path = "data/pukeImage/veryhuo.com_pkp_1.jpg"
poker_size = (150, 105)

class GameWorld:
    def __init__(self, path=background_img_path):
        self.background_img_path = path
        
    def init_world(self):
        pygame.init()
        pygame.display.set_caption("spider poker")

        self.screen = pygame.display.set_mode(
                default_size, pygame.RESIZABLE)
        self.background_img = pygame.image.load(self.background_img_path).convert()
        self.background_img = pygame.transform.scale(self.background_img, default_size)
        self.screen.blit(self.background_img, (0, 0))
        return 

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    return 
                pygame.display.flip()

    def add_poker(self, poker):
        self.screen.blit(poker.data(), poker.pos())
        return 

    def add_pokers(self, pokers):
        return 

class Poker:
    def __init__(self, path=poker_path):
        self.path = path

    def load(self):
        self.img = pygame.image.load(self.path).convert()
        self.img = pygame.transform.scale(self.img, poker_size)
        return 

    def data(self):
        return self.img

    def pos(self):
        return (60, 100) 

def start():
    game_world = GameWorld()
    game_world.init_world()
    
    poker = Poker()
    poker.load()
    game_world.add_poker(poker)
    
    game_world.start()
    return 
    

if __name__ == '__main__':
    start()




