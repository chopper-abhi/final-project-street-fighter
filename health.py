import pygame

class HealthBar:
    def __init__(self, team):
        self.team = team
        self.surface = pygame.Surface((120, 60), pygame.SRCALPHA)
        self.health = 100
        self.direction = 1 if team == (255, 0, 0) else -1
    def draw(self):
        self.surface.fill((0, 0, 0, 0))
        d = self.direction
        pygame.draw.rect(self.surface, (255, 255, 255), (0, 0, 120, 60), width=2)
    