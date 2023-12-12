import pygame
import webbrowser
from button import Button
from text import Text
from firts_track import FirtsTrack
from second_track import SecondTrack

class InterfazDijkstra:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1350, 800))  
        self.BLACK = (0,0,0)
        self.WHITE = (255, 255, 255)
        self.firts_track = FirtsTrack()
        self.second_track = SecondTrack()
    
    def options_dijkstra(self):
        screen_width = 1350
        screen_height = 800
        button_height = 45
        pygame.display.set_caption("Final project")
        fondo = pygame.image.load('images/fondo.jpg')
        button_y = (screen_height - button_height) // 2
        button_home = Button(1305, 730, 'images/home.jpeg', '', 0, (0,0,0), (0,0,0))

        font_option = pygame.font.Font(None, 70)

        button_one = Button((((screen_width / 2)- 74) - 250), button_y, 'images/buttonf.jpeg', 'Pista uno', 27, self.WHITE, (220,220,220))
        button_two = Button((((screen_width / 2)- 74) + 250), button_y, 'images/buttonf.jpeg', 'Pista dos', 27, self.WHITE, (220,220,220))

        text_option =  Text(380, 200, 'Elige la pista de pacman', font_option, self.BLACK)

        icon_git = pygame.image.load('images/git.jpg')
        font_git = pygame.font.Font(None, 25)
        text_git = Text(screen_width/2, 781, 'juancampos012', font_git, self.BLACK)
        click_area = pygame.Rect(0, screen_height-25, screen_width, 25)
        url = 'https://github.com/juancampos012/final_project_python'

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_home.is_clicked():
                        running = False
                    elif button_one.is_clicked():
                        running = False
                        self.firts_track.interfaz_firts_track()
                    elif button_two.is_clicked():
                        running = False
                        self.second_track.interfaz_second_track()
                    if click_area.collidepoint(event.pos):
                        webbrowser.open(url)

            self.screen.blit(fondo, (0,0))
            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))
            self.screen.blit(icon_git, (610, 775))
            text_git.draw(self.screen)
            button_home.draw(self.screen)

            text_option.draw(self.screen)

            button_one.draw(self.screen)
            button_two.draw(self.screen)

            pygame.display.update()
