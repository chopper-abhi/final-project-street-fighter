import sys, pygame
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from man import Man

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clk = pygame.time.Clock()

man1 = Man(100, 520, (255, 0, 0),
           {'left': pygame.K_a, 'right': pygame.K_d, 'jump': pygame.K_w},
           direction=1)

man2 = Man(1300, 520, (0, 0, 255),
           {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP},
           direction=-1)

def check_collision(a, b):
    mask_a = pygame.mask.from_surface(a.surface)
    mask_b = pygame.mask.from_surface(b.surface)
    pos_a = a.get_blit_pos()
    pos_b = b.get_blit_pos()
    offset = (pos_b[0] - pos_a[0], pos_b[1] - pos_a[1])
    return mask_a.overlap(mask_b, offset) is not None

run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    old_x1, old_y1 = man1.x, man1.changed_y
    old_x2, old_y2 = man2.x, man2.changed_y

    man1.move(True)
    man2.move(True)

    man1._draw_to_surface()
    man2._draw_to_surface()

    if check_collision(man1, man2):
        man1.x = old_x1
        man2.x = old_x2

    old_y1 = man1.changed_y
    old_y2 = man2.changed_y

    if man1.is_jumping:
        man1.jump(True)

    if man2.is_jumping:
        man2.jump(True)

    man1._draw_to_surface()
    man2._draw_to_surface()

    if check_collision(man1, man2):
        man1.changed_y = old_y1
        man2.changed_y = old_y2

        if man1.v < 0:
            man1.v = 0

        if man2.v < 0:
            man2.v = 0

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (100, 0, 0), [0, 700, 1400, 100])

    for i in range(1, 14):
        pygame.draw.line(screen, (125, 125, 130), (i * 100, 0), (i * 100, 700))

    for i in range(1, 7):
        pygame.draw.line(screen, (125, 125, 130), (0, i * 100), (1400, i * 100))

    man1.draw(screen)
    man2.draw(screen)

    pygame.display.flip()
    clk.tick(30)

pygame.quit()