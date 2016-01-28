import pygame
import random

pygame.init()


class CardPlayer:

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
