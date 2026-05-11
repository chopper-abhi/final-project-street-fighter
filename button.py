import pygame

class Button:
    def __init__(self, text, pos, size, color, font_size=30):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.font_size = font_size
        self.surface = pygame.Surface(size)
        self.font = pygame.font.SysFont("Garamond", font_size)
        self.rendered_text = self.font.render(text, True, (255, 255, 255))
        self.rect = self.surface.get_rect(topleft=pos)

    def draw(self, screen):
        self.surface.fill(self.color)
        text_rect = self.rendered_text.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.surface.blit(self.rendered_text, text_rect)
        screen.blit(self.surface, self.pos)

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
        return False