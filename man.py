import pygame

class Man:
    def __init__(self, x, y, color, controls, direction=1):
        self.x = x
        self.y = y
        self.changed_y = y
        self.team = color
        self.direction = direction
        self.controls = controls
        self.is_jumping = False
        self.is_punching = False
        self.is_hit = False
        self.moving = False
        self.v = 0
        self.grav = 3
        self.count = 0
        self.surface = pygame.Surface((120, 210), pygame.SRCALPHA)
        self.health = 100
        self.counter = 0

    def _draw_to_surface(self):
        self.surface.fill((0, 0, 0, 0))
        d = self.direction
        cx, cy = 60, 30

        if self.is_jumping:
            pygame.draw.circle(self.surface, self.team, (cx, cy), 30)
            pygame.draw.line(self.surface, self.team, (cx, cy), (cx, cy+90), width=16)
            pygame.draw.line(self.surface, self.team, (cx, cy+35), (cx+10*d, cy+65), width=5)
            pygame.draw.line(self.surface, self.team, (cx+10*d, cy+65), (cx+35*d, cy+40), width=10)
            pygame.draw.line(self.surface, self.team, (cx, cy+55), (cx+20*d, cy+66), width=10)
            pygame.draw.line(self.surface, self.team, (cx+20*d, cy+66), (cx+45*d, cy+48), width=10)
            pygame.draw.line(self.surface, self.team, (cx, cy+90), (cx+25*d, cy+115), width=16)
            pygame.draw.line(self.surface, self.team, (cx+25*d, cy+115), (cx+5*d, cy+155), width=16)
        elif self.is_punching:
            pygame.draw.circle(self.surface, self.team, (cx, cy), 30)
            pygame.draw.line(self.surface, self.team, (cx, cy), (cx, cy+120), width=16)
            pygame.draw.line(self.surface, self.team, (cx, cy+35), (cx+10*d, cy+65), width=5)
            pygame.draw.line(self.surface, self.team, (cx+10*d, cy+65), (cx+35*d, cy+40), width=10)
            pygame.draw.line(self.surface, self.team, (cx, cy+55), (cx+55*d, cy+55), width=10)
            pygame.draw.line(self.surface, self.team, (cx-3*d, cy+120), (cx-20*d, cy+200), width=10)
            pygame.draw.line(self.surface, self.team, (cx+3*d, cy+120), (cx+20*d, cy+200), width=10)
        elif self.is_hit:
            pygame.draw.circle(self.surface, self.team, (cx-30*d, cy), 30)
            pygame.draw.line(self.surface, self.team, (cx-30*d, cy), (cx, cy+35), width=16)
            pygame.draw.line(self.surface, self.team, (cx, cy+35), (cx, cy+120), width=16)
            pygame.draw.line(self.surface, self.team, (cx+10*d, cy+65), (cx+35*d, cy+40), width=10)
            pygame.draw.line(self.surface, self.team, (cx, cy+55), (cx+20*d, cy+66), width=10)
            pygame.draw.line(self.surface, self.team, (cx+20*d, cy+66), (cx+45*d, cy+48), width=10)
            pygame.draw.line(self.surface, self.team, (cx-3*d, cy+120), (cx-20*d, cy+200), width=10)
            pygame.draw.line(self.surface, self.team, (cx+3*d, cy+120), (cx+20*d, cy+200), width=10)
            self.counter += 1
            self.is_hit = False if self.counter >= 2 else True
            self.counter = 0 if self.counter >= 2 else self.counter
        else:
            pygame.draw.circle(self.surface, self.team, (cx, cy), 30)
            pygame.draw.line(self.surface, self.team, (cx, cy), (cx, cy+120), width=16)
            pygame.draw.line(self.surface, self.team, (cx, cy+35), (cx+10*d, cy+65), width=5)
            pygame.draw.line(self.surface, self.team, (cx+10*d, cy+65), (cx+35*d, cy+40), width=10)
            pygame.draw.line(self.surface, self.team, (cx, cy+55), (cx+20*d, cy+66), width=10)
            pygame.draw.line(self.surface, self.team, (cx+20*d, cy+66), (cx+45*d, cy+48), width=10)
            pygame.draw.line(self.surface, self.team, (cx-3*d, cy+120), (cx-20*d, cy+200), width=10)
            pygame.draw.line(self.surface, self.team, (cx+3*d, cy+120), (cx+20*d, cy+200), width=10)

    def get_blit_pos(self):
        return (self.x - 60, self.changed_y - 30)

    def draw(self, canvas):
        self._draw_to_surface()
        canvas.blit(self.surface, self.get_blit_pos())

    def jump(self, condition_move):
        if condition_move:
            self.changed_y += self.v
            self.v += self.grav
            if self.changed_y >= self.y:
                self.changed_y = self.y
                self.v = 0
                self.is_jumping = False
                self.count = 0

    def move(self, condition_move, events):
        self.moving = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.controls['punch'] and self.count == 0 and condition_move:
                    self.is_punching = True
                    self.is_moving = True
        keys = pygame.key.get_pressed()
        if keys[self.controls['left']] and condition_move and self.x > 30:
            self.x -= 5
            self.moving = True
        if keys[self.controls['right']] and condition_move and self.x < 1370:
            self.x += 5
            self.moving = True
        if keys[self.controls['jump']] and self.count == 0 and condition_move:
            self.count += 1
            self.is_jumping = True
            self.v = -27
        if keys[self.controls['block']] and self.cooldown_block == 0:
            self.is_blocking = True
            self.cooldown_block = 30