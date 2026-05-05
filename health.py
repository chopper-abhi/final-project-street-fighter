import pygame

class HealthBar:
    def __init__(self, team):
        self.team = team
        self.surface = pygame.Surface((120, 60), pygame.SRCALPHA)
        self.health = 100
    def _draw_to_surface(self):
        self.surface.fill((0, 0, 0, 0))
        if self.team == (255, 0, 0):
            pygame.draw.rect(self.surface, (25, 25, 25), ((50, 50), (600, 30)), width=5)
            pygame.draw.rect(self.surface, self.team, ((55, 55), (590, 20)), width=0)
        else:
            pygame.draw.rect(self.surface, (25, 25, 25), ((750, 50), (600, 30)), width=5)
            pygame.draw.rect(self.surface, self.team, ((755, 55), (590, 20)), width=0)
    def draw(self, canvas):
        self._draw_to_surface()
        canvas.blit(self.surface, self.get_blit_pos())
    def get_blit_pos(self):
        return (50, 50) if self.team == (255, 0, 0) else (750, 50)