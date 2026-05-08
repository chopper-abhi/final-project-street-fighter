import sys, pygame
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from man import Man
from health import HealthBar

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

pygame.init()
pygame.key.set_repeat(0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clk = pygame.time.Clock()

man1 = Man(100, 520, (255, 0, 0),
           {'left': pygame.K_a, 'right': pygame.K_d, 'jump': pygame.K_w, 'punch': pygame.K_1, 'block': pygame.K_2},
           direction=1)

man2 = Man(1300, 520, (0, 0, 255),
           {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP, 'punch': pygame.K_COMMA, 'block': pygame.K_PERIOD},
           direction=-1)

health_bar_a = HealthBar((255, 0, 0))
health_bar_b = HealthBar((0, 0, 255))

def check_collision(a, b):
    x_a = a.get_blit_pos()[0]
    y_a = a.get_blit_pos()[1]
    x_b = b.get_blit_pos()[0]
    y_b = b.get_blit_pos()[1]
    overlap_a = 55 if a.is_punching else 45
    overlap_b = 55 if b.is_punching else 45
    return not (x_a + overlap_a < x_b - overlap_b)

run = True
gameover = False
gameover_counter = 0

while run:
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            run = False
    run = False if (gameover and gameover_counter >= 30**10**10**10**10**10**10**10) else True
    old_x1, old_y1 = man1.x, man1.changed_y
    old_x2, old_y2 = man2.x, man2.changed_y

    man1.move(True, events, gameover)
    man2.move(True, events, gameover)

    old_y1 = man1.changed_y
    old_y2 = man2.changed_y

    if man1.is_jumping:
        man1.jump(True, gameover)

    if man2.is_jumping:
        man2.jump(True, gameover)

    if check_collision(man1, man2):
        if man1.is_punching and not man2.is_blocking:
            man2.health -= 5
            health_bar_b.health -= 5
            man2.x += 10
            man2.is_hit = True
        if man2.is_punching and not man1.is_blocking:
            man1.health -= 5
            health_bar_a.health -= 5
            man1.x -= 10
            man1.is_hit = True
        man1.x = old_x1
        man2.x = old_x2
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

    man1.draw(screen, gameover)
    man2.draw(screen, gameover)

    if man1.is_punching:
        man1.is_punching = False
    if man2.is_punching:
        man2.is_punching = False
    man1.counter_block += 1
    if man1.counter_block >= 10:
        man1.is_blocking = False
    man2.counter_block += 1
    if man2.counter_block >= 10:
        man2.is_blocking = False
    health_bar_a.draw(screen, gameover)
    health_bar_b.draw(screen, gameover)

    gameover_counter += 1 if gameover else 0

    if man1.health <= 0:
        run = False
        font = pygame.font.SysFont(None, 74)
        text = font.render("Man 2 Wins!", True, (0, 0, 0))
        screen.blit(text, (500, 350))
        gameover = True
    if man2.health <= 0:
        run = False
        font = pygame.font.SysFont(None, 74)
        text = font.render("Man 1 Wins!", True, (0, 0, 0))
        screen.blit(text, (500, 350))
        gameover = True
    
    pygame.display.flip()
    clk.tick(30)
while run:
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            run = False
    
    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (100, 0, 0), [0, 700, 1400, 100])

    for i in range(1, 14):
        pygame.draw.line(screen, (125, 125, 130), (i * 100, 0), (i * 100, 700))

    for i in range(1, 7):
        pygame.draw.line(screen, (125, 125, 130), (0, i * 100), (1400, i * 100))
    
    if man1.health <= 0:
        font = pygame.font.SysFont(None, 74)
        text = font.render("Man 2 Wins!", True, (0, 0, 0))
        screen.blit(text, (500, 350))
    if man2.health <= 0:
        font = pygame.font.SysFont(None, 74)
        text = font.render("Man 1 Wins!", True, (0, 0, 0))
        screen.blit(text, (500, 350))
    
    pygame.display.flip()
    clk.tick(30)

pygame.quit()