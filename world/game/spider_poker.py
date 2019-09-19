#!/usr/bin/python
# coding=utf-8
import os
import random
import sys

import pygame
from pygame.locals import *

default_width = 1080
default_height = 720
default_size = (1080, 720)
background_img_path = "data\\background.jpeg"
poker_dir = "data\\pukeImage"
poker_path = "data/pukeImage/veryhuo.com_pkp_1.jpg"
poker_size = (150, 105)


def random_position():
    width = random.randint(0, default_width)
    height = random.randint(0, default_height)
    return width, height


class PokerSource:
    def __init__(self, resource_dir):
        self.resource_dir = resource_dir
        self.path_list = []
        return

    def load_resource(self):
        file_list = os.listdir(self.resource_dir)
        for f in file_list:
            file_path = os.path.join(self.resource_dir, f)
            self.path_list.append(file_path)
        print self.path_list
        return True


class GameWorld:
    def __init__(self, path=background_img_path):
        self.background_img_path = path
        self.screen = pygame.display.set_mode(
            default_size, pygame.RESIZABLE)
        self.background_img = pygame.image.load(self.background_img_path).convert()
        self.background_img = pygame.transform.scale(self.background_img, default_size)
        self.screen.blit(self.background_img, (0, 0))
        pygame.init()
        pygame.display.set_caption("spider poker")

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    return 
                pygame.display.flip()

    def add_poker(self, poker):
        self.screen.blit(poker.data(), poker.position())
        return 

    def add_pokers(self, pokers):
        for poker in pokers:
            self.add_poker(poker)
        return


class PokerManager:
    def __init__(self):
        self.pokers = []
        self.poker_source = PokerSource(poker_dir)
        return

    def load(self):
        if not self.poker_source.load_resource():
            print "load resource fail"
            return False

        for path in self.poker_source.path_list:
            poker = Poker(path)
            self.pokers.append(poker)
        return True


class Poker:
    def __init__(self, path=poker_path):
        self.path = path
        self.img = pygame.image.load(self.path).convert()
        self.img = pygame.transform.scale(self.img, poker_size)
        self.pos = random_position()

    def data(self):
        return self.img

    def position(self):
        return self.pos


def start():
    game_world = GameWorld()

    # poker = Poker()
    # game_world.add_poker(poker)
    poker_manager = PokerManager()
    poker_manager.load()
    game_world.add_pokers(poker_manager.pokers)
    
    game_world.start()
    return 
    

if __name__ == '__main__':
    start()




