import sys, pygame
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from man import Man
from health import HealthBar
from button import Button

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
while run:
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            run = False
    screen.fill((200, 200, 200))
    for i in range(1, 14):
        pygame.draw.line(screen, (125, 125, 130), (i * 100, 0), (i * 100, 800))
    for i in range(1, 8):
        pygame.draw.line(screen, (125, 125, 130), (0, i * 100), (1400, i * 100))
    title_font = pygame.font.SysFont("Impact", 200)
    title_text = title_font.render("Street Fighter", True, (50, 5, 0))
    screen.blit(title_text, (150, 50))
    play = Button("Start Game", (450, 300), (500, 200), (150, 0, 0), font_size=100)
    info = Button("Instructions", (500, 550), (400, 100), (150, 150, 255), font_size=75)
    if play.is_clicked(events):
        run = False
    if info.is_clicked(events):
        info_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        run_info = True
        while run_info:
            events_info = pygame.event.get()
            for e in events_info:
                if e.type == pygame.QUIT:
                    run_info = False

            info_screen.fill((200, 200, 200))

            instructions_font = pygame.font.SysFont("Garamond", 75)

            instructions_text = (
                "Player 1: A (left), D (right), W (jump), 1 (punch), 2 (block). "
                "Player 2: Left Arrow (left), Right Arrow (right), Up Arrow (jump), "
                "Comma (punch), Period (block). Punch: 5 damage, Punch while opponent "
                "jumping: 7 damage, Block: nullifies punch damage. First player to "
                "reduce the opponent's health to 0 wins!"
            )
            words = instructions_text.split(" ")
            lines = []
            current_line = ""

            for word in words:
                test_line = current_line + word + " "
                test_surface = instructions_font.render(test_line, True, (0, 0, 0))

                if test_surface.get_width() > 1200:
                    lines.append(current_line)
                    current_line = word + " "
                else:
                    current_line = test_line

            lines.append(current_line)
            
            for i, line in enumerate(lines):
                text_surface = instructions_font.render(line, True, (0, 0, 0), None)
                info_screen.blit(text_surface, (100, 200 + i * 90))
            pygame.display.flip()
    play.draw(screen)
    info.draw(screen)
    pygame.display.flip()
    clk.tick(30)

run = True
gameover = False
while run:
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            run = False
    old_x1 = man1.x
    old_x2 = man2.x

    man1.move(True, events, gameover)
    man2.move(True, events, gameover)

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
            if man2.is_jumping:
                man2.health -= 2
                health_bar_b.health -= 2
        if man2.is_punching and not man1.is_blocking:
            man1.health -= 5
            health_bar_a.health -= 5
            man1.x -= 10
            man1.is_hit = True
            if man1.is_jumping:
                man1.health -= 2
                health_bar_a.health -= 2
        man1.x = old_x1
        man2.x = old_x2

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

    if man1.health <= 0 or man2.health <= 0:
        run = False
        gameover = True
    
    pygame.display.flip()
    clk.tick(30)
run = True
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
    
    man1.draw(screen, False)
    man2.draw(screen, False)
    health_bar_a.draw(screen, False)
    health_bar_b.draw(screen, False)

    if man1.health <= 0:
        font = pygame.font.SysFont("Garamond", 74)
        text = font.render("Blue Wins!", True, (0, 0, 255))
        screen.blit(text, (520, 350))
    if man2.health <= 0:
        font = pygame.font.SysFont("Garamond", 74)
        text = font.render("Red Wins!", True, (255, 0, 0))
        screen.blit(text, (520, 350))
    
    pygame.display.flip()
    clk.tick(30)

pygame.quit()