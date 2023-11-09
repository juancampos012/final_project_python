import pygame

class Text:
    def __init__(self, x, y, text, font, color):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.color = color
        self.rendered_text = font.render(text, True, color)
        self.rect = self.rendered_text.get_rect()
        self.rect.topleft = (x, y)

    def set_text(self, text):
        self.text = text
        self.rendered_text = self.font.render(text, True, self.color)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.rect)

    def clicked_on_text(self, pos):
        text_rect = self.rendered_text.get_rect()
        text_rect.topleft = (self.x, self.y)
        return text_rect.collidepoint(pos)