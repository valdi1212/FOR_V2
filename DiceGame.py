import pygame
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
clicked = False
show_hidden = False
player = Player(150)
computer = Player(240)

# creating buttons
reroll_msg = myfont.render("Reroll", 1, WHITE)
button_reroll = reroll_msg.get_rect()
button_reroll.x = 150
button_reroll.y = 350

show_msg = myfont.render("Show", 1, WHITE)
button_show = show_msg.get_rect()
button_show.x = 300
button_show.y = 350

result_msg = myfont.render("Results", 1, WHITE)
button_result = result_msg.get_rect()
button_result.x = 420
button_result.y = 350

while running:

    # drawing buttons
    pygame.draw.rect(window, BLACK, button_reroll)
    window.blit(reroll_msg, (button_reroll.x, button_reroll.y))

    pygame.draw.rect(window, BLACK, button_show)
    window.blit(show_msg, (button_show.x, button_show.y))

    pygame.draw.rect(window, BLACK, button_result)
    window.blit(result_msg, (button_result.x, button_result.y))

    for i in range(0, 5):
        pygame.draw.rect(window, WHITE, player.dice[i])
        pygame.draw.rect(window, WHITE, computer.dice[i])
        window.blit(computer.labels[i], computer.labelPos[i])
    if show_hidden:
        for i in range(0, 5):
            window.blit(player.labels[i], player.labelPos[i])
    else:
        for i in range(0, 4):
            window.blit(player.labels[i], player.labelPos[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON and clicked is False:
            pos = pygame.mouse.get_pos()
            if player.dice[4].collidepoint(pos) and show_hidden is False:
                player.die_roll(5)
                show_hidden = True
                clicked = True
                print("Clicked hidden dice")
            elif button_reroll.collidepoint(pos) and show_hidden is False:
                player.dice_roll()
                clicked = True
                print("Clicked reroll button")
            elif button_show.collidepoint(pos) and show_hidden is False:
                show_hidden = True
                clicked = True
                print("Clicked show button")
            elif button_result.collidepoint(pos):
                print("Your score: %d" % sum(player.num))
                print("The computer's score: %d" % sum(computer.num))
                if sum(player.num) > sum(computer.num):
                    print("You win!")
                elif sum(player.num) < sum(computer.num):
                    print("The computer wins!")
                elif sum(player.num) == sum(computer.num):
                    print("You tied.")
                running = False

    pygame.display.update()

pygame.quit()
