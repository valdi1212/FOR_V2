import pygame
from src.CardPlayer import CardPlayer

# setting up pygame
pygame.init()
window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Card game")

# creating constants
LEFT_BUTTON = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FOREST_GREEN = (34, 139, 34)

window.fill(FOREST_GREEN)

# creating bool var and player objects
running = True
clicked = False
# TODO: make CardPlayer class actually usable

while running:
    # TODO: Render the cards
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        # TODO: call functions that would display the cards

    pygame.display.update()

pygame.quit()
