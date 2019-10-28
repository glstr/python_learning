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
background_img_path = "data/background.jpeg"
poker_dir = "data/pukeImage"

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

def get_center_postion(top_left, size):
    return top_left


class Poker(pygame.sprite.Sprite):
    poker_size = (60, 80)
    step_size = 20 

    def __init__(self, poker_path, position):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.path = poker_path
        self.position = position
        self.image = load_image(poker_path, self.poker_size)
        self.rect = pygame.Rect(position, self.poker_size)
        self.rect.center = position
        self.child = None
        self.parent = None
        self.poker_type = ""
        self.poker_value = 1
        self.block_index = -1

    def set_block_index(self, index):
        self.block_index = index
        if self.child:
            self.child.set_block_index(index)

    def get_block_index(self):
        return self.block_index

    def set_child(self, poker):
        if self.child:
            print "error: had a child"
            return 

        self.child = poker
        self.child.set_position(self._get_child_position())

    def get_child(self):
        return self.child
    
    def remove_child(self):
        self.child = None

    def set_parent(self, poker):
        if self.parent:
            self.parent.remove_child()     

        self.parent = poker
        
        if poker:
            poker.set_child(self)

    def remove_parent(self):
        self.parent = None

    def get_parent(self):
        return self.parent

    def get_children(self):
        children = [self]
        if self.child:
            children.append(self.child)
            children + self.child.get_children()
        return children

    def last_child(self):
        if self.child:
            return self.child.last_child()
        return self

    def set_position(self, position):
        self.position = position
        if self.child:
            self.child.set_position(self._get_child_position())
        self.move_to_center_position(self.position)

    def reset_position(self):
        self.move_to_center_position(self.position)
        pass

    def move_to_center_position(self, position):
        self.rect = self.image.get_rect(center=position)
        if self.child:
            self.child.move_to_center_position(self._get_child_position(position))
        return

    def can_move(self):
        pass

    def update(self, *args):
        pass

    def _get_child_position(self, cur_position=None):
        if cur_position:
            return cur_position[0], cur_position[1] + self.step_size
        return self.position[0], self.position[1] + self.step_size


class MouseClicker(pygame.sprite.Sprite):
    clicker_size = (0.1, 0.1)

    def __init__(self, pos):
        # pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = pygame.Rect(pos, self.clicker_size)
        self.clicked = False
        self.picked = False
        self.picked_poker = None

    def click(self, pos):
        self.clicked = True
        self.rect.center = pos

    def pick(self, poker):
        self.picked = True
        self.picked_poker = poker

    def move(self, pos):
        self.picked_poker.move_to_center_position(pos)

    def move_pick_poker_to_front(self, all_objects):
        poker_children = self.picked_poker.get_children()
        print "poker children"
        print "child num:", len(poker_children)
        for poker in poker_children:
            print "move to front"
            all_objects.move_to_front(poker)

    def update(self, pos):
        self.rect.center = pos

    def get_picked_poker(self):
        return self.picked_poker

    def reset(self):
        self.clicked = False
        self.picked = False
        self.picked_pokers = None


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
        self.poker_block_front = []
        self.poker_block_back = []
        self.block_position = []
        self.pokers_path = ()
        step = 2
        path = "./data/pukeImage/bg.jpeg"
        for i in range(1, step * self.block_num, step):
            topleft_position = [50 * i, 50]
            rect = pygame.Rect(topleft_position, self.block_size)
            # rect = Poker(path, topleft_position)
            rect.center = topleft_position
            pygame.draw.rect(self.image, self.block_color, rect)

            center_position = get_center_postion(topleft_position, self.block_size)
            self.block_position.append(center_position)

    def load_pokers(self, pokers_path):
        self.pokers_path = pokers_path
        num = 0
        for poker_path in pokers_path:
            if num >= self.block_num:
                break
            poker = Poker(poker_path, self.block_position[num])
            poker.set_block_index(num)
            self.poker_block_front.append(poker)
            self.poker_block_back.append(poker)
            num = num + 1
        self.start = True
        self.cur_poker_num = num + 1

    def more_pokers(self):
        num = self.block_num
        for i in range(0, num):
            pokers_path_index = (i + self.cur_poker_num) % self.pokers_num
            poker = Poker(self.pokers_path[pokers_path_index], (0, 0))
            block_index = i % self.block_num

            poker.set_block_index(block_index)
            poker.set_parent(self.poker_block_back[block_index])
            self.poker_block_back[block_index] = poker

        self.cur_poker_num = self.cur_poker_num + num

    def move_to_block(self, moving_poker):
        moving_poker_index = moving_poker.get_block_index()
        print moving_poker.path
        print "move:", moving_poker_index
        has_move = False
        for index, poker in enumerate(self.poker_block_back):
            if pygame.sprite.collide_rect(poker, moving_poker) and \
                    index != moving_poker_index:
                last_child = moving_poker.last_child()
                if last_child.get_child() != None:
                    print "moving to block fail"
                    print "last child:", last_child.path
                    print "child:", last_child.get_child().path
                    return 
                if last_child != self.poker_block_back[moving_poker_index]:
                    print "moving to block fail"
                    print "last child:", last_child.path
                    print "block back:", self.poker_block_back[moving_poker_index].path
                    return 

                parent_poker = moving_poker.get_parent()
                self.poker_block_back[moving_poker_index] = parent_poker

                moving_poker.set_parent(poker)
                moving_poker.set_block_index(index)
                self.poker_block_back[index] = moving_poker.last_child()
                has_move = True
                break
        if not has_move:
            moving_poker.reset_position()


def start():
    pygame.init()
    screen = pygame.display.set_mode(
        default_size, pygame.RESIZABLE)
    pygame.display.set_caption("spider poker")

    # game object group
    pokers = pygame.sprite.Group()
    all_objects = pygame.sprite.LayeredUpdates()

    pokers_path = load_resource(poker_dir)
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

        if not mouse1 and mouse_clicker.clicked:
            #move poker 
            card_table.move_to_block(mouse_clicker.get_picked_poker())
            mouse_clicker.reset()

        if mouse3 and more_pokers:
            card_table.more_pokers()
            more_pokers = False

        if not mouse3:
            more_pokers = True

        if not mouse_clicker.clicked and mouse1:
            mouse_clicker.click(pos)
            choose_pokers = pygame.sprite.spritecollide(mouse_clicker, pokers, False)
            if len(choose_pokers) == 0:
                continue
            choose_poker = choose_pokers[0]
            mouse_clicker.pick(choose_poker)
            mouse_clicker.move_pick_poker_to_front(all_objects)
            
        if mouse_clicker.picked:
            #check with poker block
            mouse_clicker.move(pos)

        # all_objects.clear(screen, background_img)
        all_objects.update()
        # draw the scene
        dirty = all_objects.draw(screen)
        pygame.display.update(dirty)


if __name__ == '__main__':
    start()




