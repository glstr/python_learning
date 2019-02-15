#!/usr/bin/python
# coding=utf-8

import sys
import time

import pygame

default_size = (540, 960)
star_size = (30, 30)


class RoseRain:
    def __init__(self):
        self.screen = ""
        self.background = ""

    def init_all(self):
        pygame.init()
        # init background
        self.init_background()
    
    def init_background(self):
        self.screen = pygame.display.set_mode(
                default_size, pygame.RESIZABLE)
        self.background = pygame.image.load("data/rose_pig_02.jpeg").convert()
        self.background = pygame.transform.scale(self.background, default_size)
        self.screen.blit(self.background, (0, 0))
        return 
    
    def game_start(self):
        roses = Roses(8, self.screen)
        roses.init()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            start = time.time()        
            self.screen.blit(self.background, (0, 0))
            roses.next_frame()
            pygame.display.flip()
            end = time.time()
            duration = start - end
            print "frame:", 1/duration
        return 


class Roses:
    def __init__(self, num, screen):
        self.default_num = num
        self.screen = screen
        self.rose = ""
        self.roses_list = []
        self.speeds = []
        self.frame_num = 0
        self.update_rose_interval = 150 

    def stat(self):
        print 'frame_num:', self.frame_num
        print 'update_rose_interval:', self.update_rose_interval
        print 'rose_num:', len(self.roses_list)
        return 
        
    def init(self):
        element = pygame.image.load("data/rose_2.jpg").convert()
        self.star = pygame.transform.scale(element, star_size)
        self.star_rect = self.star.get_rect()
        self._add_rose()
        return 

    def next_frame(self):
        self.update()
        self.screen.blits(self.roses_list)
        self._update_stat()

        # stat
        self.stat()
        return 

    def update(self):
        addr_index = 1
        n = 0
        for ele in self.roses_list:
            if self._is_width_out(ele[addr_index]):
                flag = -self.speeds[n][1]
                self.speeds[n][0] = self._get_speed(flag)
                self.speeds[n][1] = flag
                ele[addr_index] = ele[addr_index].move(self.speeds[n][0])
            else:
                ele[addr_index] = ele[addr_index].move(self.speeds[n][0])

            if self._is_height_out(ele[addr_index]):
                self.roses_list.remove(ele)
                del self.speeds[n]

            n = n + 1

        if self.frame_num % self.update_rose_interval == 0:
            self._add_rose()

    def _is_width_out(self, rect):
        if rect.left < 0 or rect.right > self.screen.get_width():
            return True
        return False

    def _is_height_out(self, rect):
        if rect.top < 0 or rect.bottom >= self.screen.get_height():
            return True
        return False

    def _get_speed(self, flag):
        if flag == -1:
            return [1, 1]
        else:
            return [-1, 1]

    def _add_rose(self):
        for i in range(self.default_num):
            speed = [100 * i, 0]
            rect = self.star_rect.move(speed)
            speed = self._get_speed(0)
            self.roses_list.append([self.star, rect])
            flag = 1
            self.speeds.append([speed, flag])
        return                 
    
    def _update_stat(self):
        self.frame_num = self.frame_num + 1
        return 


if __name__ == '__main__':
    rose_rain = RoseRain()
    rose_rain.init_all()
    rose_rain.game_start()
