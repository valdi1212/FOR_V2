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
player1 = CardPlayer(200, 600, 1, window)
player2 = CardPlayer(0, 50, 2, window)
player3 = CardPlayer(200, 0, 1, window)
player4 = CardPlayer(860, 50, 2, window)

# print list of drawn cards to check for duplicates
# CardPlayer.drawn_cards.sort()
# print(CardPlayer.drawn_cards)

while running:
    # drawing cards
    player1.draw_hand()
    player2.draw_hand()
    player3.draw_hand()
    player4.draw_hand()

    # polling events
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON and clicked is False:
        clicked = True
        window.fill(FOREST_GREEN)
        CardPlayer.show_cards = True
        scores = [player1.score, player2.score, player3.score, player4.score]
        if scores[0] == max(scores):
            print("Player 1(bottom) wins!")
        elif scores[1] == max(scores):
            print("Player 2(left) wins!")
        elif scores[2] == max(scores):
            print("Player 3(top) wins!")
        elif scores[3] == max(scores):
            print("Player 4(rigth) wins!")

    pygame.display.update()

pygame.quit()
