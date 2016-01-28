import pygame
import random

pygame.init()

# creating constants
FRAME_WIDTH = 81
FRAME_HEIGHT = 117

# loading in the sprites
# TODO: load the face down card image from the sheet
card_frames = []

image = pygame.image.load("src/sprites/cards.gif")
sheet_width, sheet_height = image.get_size()

for row in range(0, 4):
    for col in range(int(sheet_width / FRAME_WIDTH)):
        card_frames.append(image.subsurface((col * FRAME_WIDTH, row * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)))

number_of_sprites = len(card_frames)
print(str(number_of_sprites))


class CardPlayer:

    def __init__(self, x, y, orientation, window):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.window = window

        self.hand = []
        self.card_draw()

    def card_draw(self):
        for i in range(5):
            self.hand.append(card_frames[random.randint(0, 51)])
            # TODO: make certain you can't draw a card that's already been drawn

    def draw_hand(self):
        temp_x = 0
        temp_y = 0
        if self.orientation == 1:
            for card in self.hand:
                self.window.blit(card, (self.x + temp_x, self.y))
                temp_x += 101
        elif self.orientation == 2:
            for card in self.hand:
                self.window.blit(card, (self.x, self.y + temp_y))
                temp_y += 127

    # TODO: draw face down card stacks
