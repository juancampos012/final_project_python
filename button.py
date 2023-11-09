import pygame

class Button:
    def __init__(self, x, y, image, text, font, color1, color2):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, font)
        self.color1 = color1
        self.color2 = color2

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)  
        surface.blit(self.image, self.rect) 
        text_surface = self.font.render(self.text, True, self.get_color())
        text_rect = text_surface.get_rect(center=self.rect.center) 
        surface.blit(text_surface, text_rect) 

    def get_color(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return self.color2
        else:
            return self.color1

    def is_clicked(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]