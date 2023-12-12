import pygame
import sys
import webbrowser
from button import Button
from text import Text
import random
from graph import Graph

class FirtsTrack:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 1350, 800
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 200)

        self.grid = self.generate_new_grid()

        pygame.init()

        self.screen = pygame.display.set_mode((1350, 800))
        pygame.display.set_caption("Pac-Man - Tablero")

        self.cell_size = 35

        self.graph = Graph()

        self.pacman_img = pygame.image.load("images/pacman.png")
        self.ghost_img = pygame.image.load("images/ghost.png")
        self.cherry_img = pygame.image.load("images/cherry.png")
        self.pill_img = pygame.image.load("images/pill.png")

    def generate_new_grid(self, G=7, C=3, W=2):
        grid = [
            "*******************",
            "*        *        *",
            "* * *** *** *** * *",
            "* *   *     *   * *",
            "*** * *** *** * ***",
            "* * * *     * * * *",
            "*   * * *** * *   *",
            "* * * *  *  * * * *",
            "* * *    *    * * *",
            "P *** ******* ***  ",
            "* * *    *    * * *",
            "* * * *  *  * * * *",
            "*   * * *** * *   *",
            "* * * *     * * * *",
            "*** * *** *** * ***",
            "* *   *     *   * *",
            "* * *** *** *** * *",
            "*        *        *",
            "*******************"
        ]
        flat_grid = [list(row) for row in grid]
        empty_spaces = [(i, j) for i, row in enumerate(flat_grid) for j, cell in enumerate(row) if cell == ' ']

        random.shuffle(empty_spaces)
        for i, j in empty_spaces[:G]:
            flat_grid[i][j] = 'G'
        for i, j in empty_spaces[G:G+C]:
            flat_grid[i][j] = 'C'
        for i, j in empty_spaces[G+C:G+C+W]:
            flat_grid[i][j] = 'W'
        new_grid = [''.join(row) for row in flat_grid]
        return new_grid
    
    def draw_board_path(self):
        shortest_path = self.dijkstra((0,9),(18,9))
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == '*':
                    pygame.draw.rect(self.screen, self.BLUE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.grid[y][x] == 'P':
                    self.screen.blit(self.pacman_img, (x * self.cell_size, y * self.cell_size))
                elif self.grid[y][x] == 'W':
                    self.screen.blit(self.pill_img, (x * self.cell_size, y * self.cell_size))
                elif self.grid[y][x] == 'G':
                    self.screen.blit(self.ghost_img, (x * self.cell_size, y * self.cell_size))
                elif self.grid[y][x] == 'C':
                    self.screen.blit(self.cherry_img, (x * self.cell_size, y * self.cell_size))
                else:
                    pygame.draw.circle(self.screen, self.WHITE, (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2), 8)

        for i in range(len(shortest_path) - 1):
            pygame.draw.line(self.screen, self.WHITE, (shortest_path[i][0] * self.cell_size + self.cell_size // 2, shortest_path[i][1] * self.cell_size + self.cell_size // 2), (shortest_path[i+1][0] * self.cell_size + self.cell_size // 2, shortest_path[i+1][1] * self.cell_size + self.cell_size // 2), 5)


    def draw_board(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == '*':
                    pygame.draw.rect(self.screen, self.BLUE, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.grid[y][x] == 'P':
                    self.screen.blit(self.pacman_img, (x * self.cell_size, y * self.cell_size))
                elif self.grid[y][x] == 'W':
                    self.screen.blit(self.pill_img, (x * self.cell_size, y * self.cell_size))
                elif self.grid[y][x] == 'G':
                    self.screen.blit(self.ghost_img, (x * self.cell_size, y * self.cell_size))
                elif self.grid[y][x] == 'C':
                    self.screen.blit(self.cherry_img, (x * self.cell_size, y * self.cell_size))
                else:
                    pygame.draw.circle(self.screen, self.WHITE, (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2), 8)

    def create_graph_from_grid(self, grid):
            for j, row in enumerate(grid):
                for i, cell in enumerate(row):
                    if cell != '*':
                        weight = 1 if cell == ' ' else 1000 if cell == 'G' else 3
                        self.graph.add_node((i, j), weight=weight)
                        if i > 0 and grid[j][i-1] != '*':
                            self.graph.add_edge((i, j), (i-1, j), weight=weight)
                        if j > 0 and grid[j-1][i] != '*':
                            self.graph.add_edge((i, j), (i, j-1), weight=weight)
    
    def dijkstra(self, start, end):
        self.create_graph_from_grid(self.grid)
        shortest_paths = {start: (None, 0)}
        current_node = start
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = self.graph.graph[current_node]['edges']
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node, weight in destinations.items():
                weight = weight + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        path = path[::-1]
        return path

    def interfaz_firts_track(self):
        pygame.display.set_caption("Final project")
        fondo = pygame.image.load('images/fondo_negro.jpg')

        button_home = Button(1305, 730, 'images/home.jpeg', '', 0, (0,0,0), (0,0,0))
        icon_git = pygame.image.load('images/git.jpg')
        font_git = pygame.font.Font(None, 25)
        text_git = Text(self.WIDTH/2, 781, 'juancampos012', font_git, (0,0,0))
        click_area = pygame.Rect(0, self.HEIGHT-25, self.WIDTH, 25)
        url = 'https://github.com/juancampos012/final_project_python'

        visible_path = False

        button_execute = Button(1000, 260, 'images/buttonf.jpeg', 'ejecutar', 27, self.WHITE, (220,220,220))
        button_regenerate = Button(1000, 130, 'images/buttonf.jpeg', 'regenerar', 27, self.WHITE, (220,220,220))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_home.is_clicked():
                        running = False
                    elif button_execute.is_clicked():
                        visible_path = True
                    elif button_regenerate.is_clicked():
                        visible_path = False
                        self.grid = self.generate_new_grid()
                    elif click_area.collidepoint(event.pos):
                        webbrowser.open(url)

            self.screen.blit(fondo, (0,0))
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0, 1350-25, 800, 25))
            self.screen.blit(icon_git, (610, 775))
            text_git.draw(self.screen)
            button_home.draw(self.screen)

            button_execute.draw(self.screen)
            button_regenerate.draw(self.screen)

            if visible_path is False:
                self.draw_board()
            else:
                self.draw_board_path()
            pygame.display.update()
        



