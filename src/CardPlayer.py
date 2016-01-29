import pygame
import random

pygame.init()

# creating constants
FRAME_WIDTH = 81
FRAME_HEIGHT = 117.4

# loading in the sprites
card_frames = []

image = pygame.image.load("src/sprites/cards.gif")
sheet_width, sheet_height = image.get_size()

for row in range(0, 4):
    for col in range(int(sheet_width / FRAME_WIDTH)):
        card_frames.append(image.subsurface((col * FRAME_WIDTH, row * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)))

back_card = image.subsurface((0, 4 * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT))


class CardPlayer:
    show_cards = False
    drawn_cards = []

    def __init__(self, x, y, orientation, window):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.window = window

        self.hand = []
        self.card_draw(self.hand)
        self.score = self.calc_score()

    def card_draw(self, hand):
        num = random.randint(0, 51)
        if len(hand) != 5:
            if len(self.drawn_cards) == 0:
                hand.append(num)
                self.drawn_cards.append(num)
                return self.card_draw(hand)
            else:
                for item in self.drawn_cards:
                    if item == num:
                        return self.card_draw(hand)
                hand.append(num)
                self.drawn_cards.append(num)
                return self.card_draw(hand)
        else:
            return self.hand

    def draw_hand(self):
        temp_x = 0
        temp_y = 0
        if self.show_cards:
            if self.orientation == 1:
                for card in self.hand:
                    self.window.blit(card_frames[card], (self.x + temp_x, self.y))
                    temp_x += 101
            elif self.orientation == 2:
                for card in self.hand:
                    self.window.blit(card_frames[card], (self.x, self.y + temp_y))
                    temp_y += 127
        else:
            if self.orientation == 1:
                for i in range(5):
                    self.window.blit(back_card, (self.x + temp_x, self.y))
                    temp_x += 15
            elif self.orientation == 2:
                for i in range(5):
                    self.window.blit(back_card, (self.x, self.y + temp_y))
                    temp_y += 15

    def calc_score(self):
        temp_score = 0
        for card in self.hand:
            temp_score += ((card + 1) % 13) + 1
        return temp_score
