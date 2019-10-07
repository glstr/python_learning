#!/usr/bin/python
# coding=utf-8
import os
import random
import sys

import pygame
from pygame.locals import *

# game constants
default_width = 1080
default_height = 720
default_size = (1080, 720)
background_img_path = "data\\background.jpeg"
poker_dir = "data\\pukeImage"

main_dir = os.path.split(os.path.abspath(__file__))[0]


# tool function
def load_image(file_path, image_size):
    """load an image, prepares it for play"""
    file_path = os.path.join(main_dir, file_path)
    try:
        surface = pygame.image.load(file_path)
    except pygame.error:
        raise SystemExit('could not load image %s %s' % (file_path, pygame.get_error()))
    return pygame.transform.scale(surface.convert(), image_size)


def load_images(*files_path):
    images = []
    for file_path in files_path:
        images.append(load_image(file))
    return images


def random_position():
    left = random.randint(0, default_width)
    top = random.randint(0, default_height)
    return left, top


def load_resource(resource_dir):
    file_list = os.listdir(resource_dir)
    path_list = []
    for f in file_list:
        file_path = os.path.join(resource_dir, f)
        path_list.append(file_path)
    return path_list


class Poker(pygame.sprite.Sprite):
    poker_size = (60, 80)

    def __init__(self, poker_path, position):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.position = position
        print "init position:", position
        self.image = load_image(poker_path, self.poker_size)
        self.rect = pygame.Rect(position, self.poker_size)
        self.child = None

    def add_child(self, poker):
        self.child = poker

    def remove_child(self):
        self.child = None

    def move(self, direction):
        self.rect.move(direction)
        if self.child:
            self.child.move(direction)

    def set_center_position(self, position):
        print "position:", self.position
        self.rect = self.image.get_rect(center=position)
        child_position = (position[0], position[1] + 20)
        print "center_child_pos:", child_position
        if self.child:
            self.child.set_center_position(child_position)
        return

    def set_top_left_position(self, position):
        self.rect = self.image.get_rect(topleft=position)
        child_position = (position[0], position[1])
        print "top_self_child_pos:", child_position
        if self.child:
            self.child.set_center_position(child_position)
        return

    def can_move(self):
        pass

    def update(self, *args):
        pass

    def allocate(self, need_change, position):
        if need_change:
            self.rect = self.image.get_rect(topleft=position)
            self.position = position
            print "allocate position:", self.position
        else:
            print "position:", self.position
            self.rect = self.image.get_rect(topleft=self.position)

        if self.child:
            self.child.allocate(need_change, position)


class MouseClicker(pygame.sprite.Sprite):
    clicker_size = (0.1, 0.1)

    def __init__(self, pos):
        # pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = pygame.Rect(pos, self.clicker_size)
        self.clicked = False
        self.picked = False
        self.poker = None

    def update(self, pos):
        self.rect.center = pos

    def set_picked_poker(self, poker):
        self.poker = poker

    def reset(self):
        self.clicked = False
        self.picked = False
        if self.poker:
            self.poker.allocate(False, (0, 0))
            self.poker = None


class PokerBlock(pygame.sprite.Sprite):
    block_size = (60, 80)
    step_size = 20

    def __init__(self, position):
        self.position = position
        self.poker_group = pygame.sprite.Group()
        self.last_poker = None
        self.cur_position = position
        self.poker_num = 0

    def add_poker(self, poker):
        if self.last_poker:
            self.last_poker.add_child(poker)
        self.last_poker = poker
        self.poker_group.add(poker)
        poker.allocate(True, (self.cur_position[0], self.cur_position[1]))
        self.cur_position[1] = self.cur_position[1] + self.step_size

    def remove_poker(self, poker):
        self.poker_group.remove(poker)
        self.cur_position[1] = self.cur_position[1] - self.step_size
        pass

    def move(self, position):
        pass


class CardTable(pygame.sprite.Sprite):
    table_position = (0, 0)
    table_size = (1080, 720)
    pokers_num = 54
    block_color = pygame.Color(255, 0, 0)
    block_size = (60, 80)
    block_num = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = load_image(background_img_path, self.table_size)
        self.rect = pygame.Rect(self.table_position, self.table_size)
        self.start = False
        self.cur_poker_num = 0
        self.poker_blocks = []
        self.pokers_path = ()
        step = 2
        for i in range(1, step * self.block_num, step):
            position = [50 * i, 30]
            rect = pygame.Rect(position, self.block_size)
            pygame.draw.rect(self.image, self.block_color, rect)
            poker_block = PokerBlock(position)
            self.poker_blocks.append(poker_block)

    def load_pokers(self, pokers_path):
        self.pokers_path = pokers_path
        num = 0
        for poker_path in pokers_path:
            if num >= self.block_num:
                break
            poker = Poker(poker_path, (0, 0))
            self.poker_blocks[num].add_poker(poker)
            num = num + 1
        self.start = True
        self.cur_poker_num = num + 1

    def more_pokers(self):
        num = self.block_num
        for i in range(0, num):
            pokers_path_index = (i + self.cur_poker_num) % self.pokers_num
            poker = Poker(self.pokers_path[pokers_path_index], (0, 0))
            block_index = i % self.block_num
            self.poker_blocks[block_index].add_poker(poker)
        self.cur_poker_num = self.cur_poker_num + num


def start():
    pygame.init()
    screen = pygame.display.set_mode(
        default_size, pygame.RESIZABLE)
    pygame.display.set_caption("spider poker")

    # game object group
    pokers = pygame.sprite.Group()
    all_objects = pygame.sprite.LayeredUpdates()

    pokers_path = load_resource(poker_dir)
    print pokers_path
    Poker.containers = pokers, all_objects

    CardTable.containers = all_objects
    card_table = CardTable()
    card_table.load_pokers(pokers_path)
    all_objects.move_to_back(card_table)

    mouse_clicker = MouseClicker((0, 0))
    more_pokers = True
    # loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # process mouse event
        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        direction = pygame.mouse.get_rel()

        if not mouse1:
            mouse_clicker.reset()

        if mouse3 and more_pokers:
            card_table.more_pokers()
            more_pokers = False

        if not mouse3:
            more_pokers = True

        if not mouse_clicker.clicked and mouse1:
            print "picked"
            mouse_clicker.update(pos)
            mouse_clicker.clicked = True
            choose_pokers = pygame.sprite.spritecollide(mouse_clicker, pokers, False)
            if len(choose_pokers) == 0:
                continue
            choose_poker = choose_pokers[0]
            # all_objects.move_to_front(choose_poker)
            mouse_clicker.set_picked_poker(choose_poker)
            mouse_clicker.picked = True

        if mouse_clicker.picked:
            print "move"
            print pos
            print direction
            mouse_clicker.poker.set_center_position(pos)
            # mouse_clicker.poker.move(direction)

        # all_objects.clear(screen, background_img)
        all_objects.update()
        # draw the scene
        dirty = all_objects.draw(screen)
        pygame.display.update(dirty)


if __name__ == '__main__':
    start()




