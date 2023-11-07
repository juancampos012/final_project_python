import pygame

class TextBox:
    def __init__(self, x, y, width, height, font, text_color, input_color, cursor_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.text_color = text_color
        self.input_color = input_color
        self.cursor_color = cursor_color
        self.text = ""
        self.cursor_visible = True
        self.cursor_timer = 0
        self.active = False
        self.information = ''

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.cursor_timer = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                if self.collide_point(event.pos):
                    self.active = True
                else:
                    self.active = False

    def information_text(self):
        return self.text

    def update(self):
        if self.active:
            self.cursor_timer += 1
            if self.cursor_timer > 350:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.input_color, (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 0)
        input_text = self.font.render(self.text, True, self.text_color)
        text_rect = input_text.get_rect()
        
        # Ajusta la posición vertical del texto para centrarlo
        text_rect.topleft = (self.x, self.y + (self.height - text_rect.height) // 2)
        
        surface.blit(input_text, text_rect)
        
        if self.active and self.cursor_visible:
            cursor_x = text_rect.x + text_rect.width
            cursor_y = text_rect.centery
            pygame.draw.line(surface, self.cursor_color, (cursor_x, cursor_y - 8), (cursor_x, cursor_y + 8), 1)

    def collide_point(self, pos):
        return self.x - 5 <= pos[0] <= self.x + self.width + 5 and self.y - 5 <= pos[1] <= self.y + self.height + 5