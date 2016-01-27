import pygame
import random

pygame.init()


class Player:
    myfont = pygame.font.SysFont("Monospace", 20)

    def __init__(self, y):
        self.num = []
        self.dice = []
        self.labels = []
        self.labelPos = []
        self.y = y

        self.label_init()
        self.dice_init()

    def label_init(self):
        for i in range(0, 5):
            self.num.append(random.randint(1, 6))
            self.labels.append(self.myfont.render(str(self.num[i]), 1, (0, 0, 0)))

    def dice_init(self):
        x_start = 150
        for i in range(0, 5):
            self.dice.append(pygame.Rect(x_start, self.y, 60, 60))
            self.labelPos.append((x_start + 20, self.y + 20))
            x_start += 70

    def dice_roll(self):
        for i in range(0, 5):
            self.num[i] = random.randint(1, 6)
            self.labels[i] = self.myfont.render(str(self.num[i]), 1, (0, 0, 0))
