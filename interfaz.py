import pygame
import webbrowser
from button import Button
from text import Text
from interfaz_binary import InterfazBinary
from interfaz_nary import InterfazNary

class Interfaz:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1350, 800))
        self.nary = InterfazNary()
        self.binary = InterfazBinary()

    def principal(self):
        screen_width = 1350
        screen_height = 800
        button_width = 148
        button_x = (screen_width - button_width) // 2
        pygame.display.set_caption("Final project")
        fondo = pygame.image.load('images/fondo.jpg')

        BLACK = (0,0,0)
        WHITE = (255, 255, 255)

        icon_git = pygame.image.load('images/git.jpg')
        font_git = pygame.font.Font(None, 25)
        text_git = Text(screen_width/2, 781, 'juancampos012', font_git, BLACK)
        click_area = pygame.Rect(0, screen_height-25, screen_width, 25)
        url = 'https://github.com/juancampos012/final_project_python'
        button_menu = Button(button_x, 175, 'images/buttonf.jpeg', 'Arboles' , 40, WHITE, (220,220,220))
        button_binary_tree = Button(button_x, 225, 'images/buttonf.jpeg', 'Binarios', 40, WHITE, (220,220,220))
        button_n_tree = Button(button_x, 275, 'images/buttonf.jpeg', 'N-arios', 40, WHITE, (220,220,220))
        button_grafos = Button(button_x, 430, 'images/buttonf.jpeg', 'grafos', 40, WHITE, (220,220,220))
        button_dijkstra = Button(button_x, 480, 'images/buttonf.jpeg', 'Dijkstra', 40, WHITE, (220,220,220))
        font_tittle = pygame.font.Font(None,50)
        text_tittle = Text(520, 60, 'Menu de opciones.', font_tittle, BLACK)

        active_desplegable_tree = False
        active_desplegable_grafo = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_menu.is_clicked() and active_desplegable_tree is True and active_desplegable_grafo is False:
                        active_desplegable_tree = False
                    elif button_menu.is_clicked() and active_desplegable_tree is False and active_desplegable_grafo is False:
                        active_desplegable_tree = True
                    elif button_grafos.is_clicked() and active_desplegable_grafo is True and active_desplegable_tree is False:
                        active_desplegable_grafo = False
                    elif button_grafos.is_clicked() and active_desplegable_grafo is False and active_desplegable_tree is False:
                        active_desplegable_grafo = True
                    elif button_grafos.is_clicked() and active_desplegable_tree is True and active_desplegable_grafo is False:
                        active_desplegable_tree = False
                        active_desplegable_grafo = True
                    elif button_menu.is_clicked() and active_desplegable_grafo is True and active_desplegable_tree is False:
                        active_desplegable_grafo = False
                        active_desplegable_tree = True
                    if click_area.collidepoint(event.pos):
                        webbrowser.open(url)

            self.screen.blit(fondo, (0,0))
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))
            self.screen.blit(icon_git, (610, 775))
            text_git.draw(self.screen)
            text_tittle.draw(self.screen)
            button_menu.draw(self.screen)
            button_grafos.draw(self.screen)
            if active_desplegable_tree is True:
                button_binary_tree.draw(self.screen)
                button_n_tree.draw(self.screen)
                if button_binary_tree.is_clicked():
                    self.binary.binary_tree()
                elif button_n_tree.is_clicked():
                    self.nary.nario_tree()
            elif active_desplegable_grafo is True:
                button_dijkstra.draw(self.screen)
            pygame.display.update()