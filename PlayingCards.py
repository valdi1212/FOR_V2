import pygame
from src.CardPlayer import CardPlayer

# setting up pygame
pygame.init()
window_size = window_width, window_height = 960, 720
window = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption("Card game")

# creating constants
LEFT_BUTTON = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FOREST_GREEN = (34, 139, 34)

window.fill(FOREST_GREEN)

# creating variables
running = True
clicked = False
timer = pygame.time.Clock()
player = CardPlayer(200, 600, 1, window)
advers1 = CardPlayer(0, 50, 2, window)
advers2 = CardPlayer(200, 0, 1, window)
advers3 = CardPlayer(860, 50, 2, window)

while running:
    player.draw_hand()
    advers1.draw_hand()
    advers2.draw_hand()
    advers3.draw_hand()
    # TODO: make the game only draw hands after the mouse is clicked
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        # TODO: call functions that would display the cards
        # TODO call function that would calculate who has highest sum and declare the winner

    pygame.display.update()

pygame.quit()
