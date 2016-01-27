import pygame
import random
from src.Player import Player

# setting up pygame
pygame.init()
window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Dice game")
myfont = pygame.font.SysFont("Monospace", 15)

# creating constants
LEFT_BUTTON = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FOREST_GREEN = (34, 139, 34)

window.fill(FOREST_GREEN)

# creating bool var and player objects
running = True
player = Player(150)
computer = Player(240)

# creating buttons
reroll_msg = myfont.render("Reroll", 1, BLACK)
button_reroll = reroll_msg.get_rect()
button_reroll.x = 150
button_reroll.y = 350

show_msg = myfont.render("Show", 1, BLACK)
button_show = show_msg.get_rect()
button_show.x = 300
button_show.y = 350

while running:

    # drawing buttons
    pygame.draw.rect(window, WHITE, button_reroll)
    window.blit(reroll_msg, (button_reroll.x, button_reroll.y))

    pygame.draw.rect(window, WHITE, button_show)
    window.blit(show_msg, (button_show.x, button_show.y))

    for i in range(0, 5):
        pygame.draw.rect(window, WHITE, player.dice[i])
        pygame.draw.rect(window, WHITE, computer.dice[i])
        window.blit(computer.labels[i], computer.labelPos[i])
    for i in range(0, 4):
        window.blit(player.labels[i], player.labelPos[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            # player.dice_roll()
            pos = pygame.mouse.get_pos()

    pygame.display.update()

pygame.quit()
