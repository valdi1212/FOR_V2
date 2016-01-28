import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

LEFT_BUTTON = 1
x = 200
y = 150
mouse_pos = (x, y)
# Access to the clock is necessary for screen speed control
clock = pygame.time.Clock()
running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        mouse_pos = pygame.mouse.get_pos()

    if x != mouse_pos[0]:
        if x > mouse_pos[0]:
            x -= 1
        else:
            x += 1
    if y != mouse_pos[1]:
        if y > mouse_pos[1]:
            y -= 1
        else:
            y += 1

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 20, 2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
