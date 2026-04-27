import sys, pygame

class Man:
    def __init__(self, x, y, team):
        self.surface = pygame.Surface((60, 170), pygame.SRCALPHA)

    def draw(self, canvas):
        self.surface.fill((0, 0, 0, 0))

        pygame.draw.circle(self.surface, self.team, (30, 25), 25)
        pygame.draw.line(self.surface, self.team, (30, 50), (30, 115), 6)
        pygame.draw.line(self.surface, self.team, (30, 65), (0, 90), 6)
        pygame.draw.line(self.surface, self.team, (30, 65), (60, 90), 6)
        pygame.draw.line(self.surface, self.team, (30, 115), (10, 165), 6)
        pygame.draw.line(self.surface, self.team, (30, 115), (50, 165), 6)

        # blit the surface onto the canvas at the object's world position
        canvas.blit(self.surface, (self.x - 30, self.changed_y - 25))

