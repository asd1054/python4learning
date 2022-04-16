from email import header


# -*- encoding: utf-8 -*-
'''
@File    :   贪吃蛇.py
@Time    :   2022/03/26 15:42:00
@Author  :   NMOON 
@Version :   1.0
@Contact :   ay1054@qq.com
@Personal:   应无所往，而生其心
@Function:   贪吃蛇小游戏
@Desc    :   使用类
'''

# here put the import lib
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake:
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    """绘制窗口

    Args:
        w (width): 宽度
        rows (行数): _description_
        surface (win): _description_
    """
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redDrawWindow(surface):
    """重制窗口绘制

    Args:
        surface (win格式): pygame中的屏幕窗口
    """
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.displayx.update()


def randomSnack(rows, items):
    pass


def mesageBox(subject, content):
    pass


def main():
    global rows, width
    width = 500
    rows = 20
    win = pygame.display.set_mode(width, width)
    s = Snake((255, 0, 0), (10, 10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redDrawWindow(win)
    pass


if __name__ == '__main__':
    print(1)
