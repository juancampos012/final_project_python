import pygame

class Alert:
    def __init__(self, mensaje, fuente, color_fondo, color_texto, x, y, duracion):
        self.mensaje = mensaje
        self.fuente = fuente
        self.color_fondo = color_fondo
        self.color_texto = color_texto
        self.x = x
        self.y = y
        self.duracion = duracion
        self.tiempo_mostrado = pygame.time.get_ticks()
        self.mostrar_alerta = False

    def draw(self, screen):
        if self.mostrar_alerta:
            ahora = pygame.time.get_ticks()
            tiempo_transcurrido = ahora - self.tiempo_mostrado

            if tiempo_transcurrido < self.duracion:
                texto = self.fuente.render(self.mensaje, True, self.color_texto)
                rectangulo = texto.get_rect(center=(self.x, self.y))
                pygame.draw.rect(screen, self.color_fondo, rectangulo)
                screen.blit(texto, rectangulo)
            else:
                self.mostrar_alerta = False