import pygame

class HealthBar:
    def __init__(self, team,y=50,width=600,height=30):
        self.team = team
        self.x = 50 if team == (255, 0, 0) else 750
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health = 100
    def _draw_to_surface(self, canvas):
        if self.team == (255, 0, 0):
            pygame.draw.rect(canvas, (25, 25, 25), self.rect, width=5)
            pygame.draw.rect(canvas, self.team, (self.x+5, self.y+5, (self.width-10)*self.health/100, self.height-10), width=0)
        else:
            pygame.draw.rect(canvas, (25, 25, 25), self.rect, width=5)
            pygame.draw.rect(canvas, self.team, (self.x+5+((100-self.health)/100)*590, self.y+5, (self.width-10)*self.health/100, self.height-10), width=0)
    def draw(self, canvas):
        self._draw_to_surface(canvas)
    def get_blit_pos(self):
        return (50, 50) if self.team == (255, 0, 0) else (750, 50)