import sys, pygame

class Man2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.changed_y = y
        self.team = (0, 0, 255)
        self.direction = -1
        self.is_jumping = False
        self.v = 0
        self.grav = 2
        self.count = 0

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.team, (self.x, self.changed_y), 30)
        pygame.draw.line(canvas, self.team, (self.x, self.changed_y), (self.x, self.changed_y+120), width=16)
        pygame.draw.line(canvas, self.team, (self.x, self.changed_y+45), (self.x+10*self.direction, self.changed_y+65), width=10)
        pygame.draw.line(canvas, self.team, (self.x+10*self.direction, self.changed_y+65), (self.x+35*self.direction, self.changed_y+40), width=10)
        pygame.draw.line(canvas, self.team, (self.x, self.changed_y+55), (self.x+20*self.direction, self.changed_y+66), width=10)
        pygame.draw.line(canvas, self.team, (self.x+20*self.direction, self.changed_y+66), (self.x+45*self.direction, self.changed_y+48), width=10)
        pygame.draw.line(canvas, self.team, (self.x-3*self.direction, self.changed_y+120), (self.x-20*self.direction, self.changed_y+200), width=10)
        pygame.draw.line(canvas, self.team, (self.x+3*self.direction, self.changed_y+120), (self.x+20*self.direction, self.changed_y+200), width=10)

    def jump(self, canvas):
        self.changed_y += self.v
        self.v += self.grav
        if self.changed_y >= self.y:
            self.changed_y = self.y
            self.v = 0
            self.is_jumping = False
            self.count = 0

    def move(self, canvas):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_UP] and self.count == 0:
            self.count += 1
            self.is_jumping = True
            self.v = -25
        #if keys[pygame.K_DOWN]:
        #    self.y += 5