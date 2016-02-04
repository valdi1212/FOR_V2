import pygame
import random

pygame.init()

window_size = 640, 480
window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Dice GUI")
myfont = pygame.font.SysFont("Monospace", 20)

LEFT_BUTTON = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FOREST_GREEN = (34, 139, 34)

window.fill(FOREST_GREEN)

dice = []
labels = []
running = True


def label_init():
    for i in range(0, 5):
        rand = random.randint(1, 6)
        labels.append(myfont.render(str(rand), 1, BLACK))


def dice_init():
    global x_start
    for i in range(0, 5):
        dice.append(pygame.Rect(x_start, 210, 60, 60))
        x_start += 70
    x_start = 150


def click_die(clicked_die):
    for i in range(0, len(dice)):
        if clicked_die == dice[i]:
            labels[i] = myfont.render(str(random.randint(1, 6)), 1, BLACK)


while running:
    x_start = 150

    if len(labels) == 0:
        label_init()
    if len(dice) == 0:
        dice_init()
    for i in range(0, 5):
        pygame.draw.rect(window, WHITE, dice[i])
        window.blit(labels[i], (x_start + 25, 235))
        x_start += 70

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            pos = pygame.mouse.get_pos()
            clicked_die = None
            for die in dice:
                if die.collidepoint(pos):
                    clicked_die = die
            if clicked_die is not None:
                click_die(clicked_die)

    pygame.display.update()

pygame.quit()
