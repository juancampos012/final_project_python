import pygame

class Checkbox:
    def __init__(self, x, y, width, height, label, font, border_color):
        checked = False
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.font = font
        self.border_color = border_color
        self.checked = checked

    def draw(self, screen):
        checkbox = pygame.Surface((self.rect.height, self.rect.height))
        checkbox.fill(pygame.Color("white"))
        pygame.draw.rect(checkbox, self.border_color, checkbox.get_rect(), 2)
        
        if self.checked:
            pygame.draw.line(checkbox, self.border_color, (5, self.rect.height // 2), (self.rect.height // 2, self.rect.height - 5), 2)
            pygame.draw.line(checkbox, self.border_color, (self.rect.height // 2, self.rect.height - 5), (self.rect.height - 5, 5), 2)

        screen.blit(checkbox, self.rect.topleft)

        label_surface = self.font.render(self.label, True, self.border_color)
        screen.blit(label_surface, (self.rect.right + 10, self.rect.centery - label_surface.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked