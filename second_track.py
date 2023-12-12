import pygame
import webbrowser
from text_box import TextBox
from button import Button
from text import Text
from alert import Alert
from graph import Graph
import sys
import random

class SecondTrack:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 1350, 800
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 200)

        self.grid = self.generate_new_grid(0,0,0)

        pygame.init()

        self.screen = pygame.display.set_mode((1350, 800))
        pygame.display.set_caption("Pac-Man - Tablero")

        self.cell_size = 35

        self.path_prim = []
        self.path_dijkstra = []

        self.graph = Graph()

        self.value_ghost = 0
        self.value_cherry = 0

        self.pacman_img = pygame.image.load("images/pacman.png")
        self.ghost_img = pygame.image.load("images/ghost.png")
        self.cherry_img = pygame.image.load("images/cherry.png")
        self.pill_img = pygame.image.load("images/pill.png")

    def generate_new_grid(self, G, C, W):
        grid = [
            "*******************",
            "*   *   * *   *   *",
            "* ***** *** ***** *",
            "*   *    *    *   *",
            "* * * ******* * * *",
            "* *      *      * *",
            "* ****** * ****** *",
            "*   *         *   *",
            "* * *** *** *** * *",
            "P *      *      *  ",
            "* * *** *** *** * *",
            "*   *         *   *",
            "* ****** * ****** *",
            "* *      *      * *",
            "* * * ******* * * *",
            "*   *    *    *   *",
            "* ***** *** ***** *",
            "*   *   * *   *   *",
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

    def draw_board_path_dijkstra(self):
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

    def draw_board_path(self):
        print('hasta aca')
        mst = self.prim((0,9))
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

        for edge in mst:
            pygame.draw.line(self.screen, self.WHITE, (edge[0][0] * self.cell_size + self.cell_size // 2, edge[0][1] * self.cell_size + self.cell_size // 2), (edge[1][0] * self.cell_size + self.cell_size // 2, edge[1][1] * self.cell_size + self.cell_size // 2), 5)

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

    def prim(self, start_node):
        self.create_graph_from_grid(self.grid)
        mst = []
        used = set([start_node])

        while len(used) != len(self.graph.graph):
            min_weight = 10000
            for node in used:
                for weight, adj_node in self.graph.graph[node]['edges'].items():
                    if adj_node not in used and weight < min_weight:
                        min_weight = weight
                        selected_nodes = (node, adj_node)
            mst.append(selected_nodes + (min_weight,))
            used.add(selected_nodes[1])

        return mst

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

    def interfaz_second_track(self):
        pygame.display.set_caption("Final project")
        fondo = pygame.image.load('images/fondo_negro.jpg')

        button_home = Button(1305, 730, 'images/home.jpeg', '', 0, (0,0,0), (0,0,0))
        icon_git = pygame.image.load('images/git.jpg')
        font_git = pygame.font.Font(None, 25)
        text_git = Text(self.WIDTH/2, 781, 'juancampos012', font_git, (0,0,0))
        click_area = pygame.Rect(0, self.HEIGHT-25, self.WIDTH, 25)
        url = 'https://github.com/juancampos012/final_project_python'

        font = pygame.font.Font(None, 20)
        font_subtittle = pygame.font.Font(None, 25)

        text_color = (0,0,0)
        input_color = self.WHITE
        cursor_color = (0,0,0)

        visible_path_dijkstra = False
        visible_path_prim = False

        button_dijkstra = Button(970, 300, 'images/buttonf.jpeg', 'Dijkstra', 27, self.WHITE, (220,220,220))

        value_ghots = TextBox(1000, 200, 300, 20, font, text_color, input_color, cursor_color)
        value_cherry = TextBox(1000, 250, 300, 20, font, text_color, input_color, cursor_color)
        value_pill = TextBox(1000, 150, 300, 20, font, text_color, input_color, cursor_color)

        text_number_pill = Text(845, 153, 'Cantidad Pildoras:', font, self.WHITE)
        text_number_ghost = Text(845, 203, 'Cantidad Fantasmas:', font, self.WHITE)
        text_number_cherry = Text(845, 253, 'Cantidad Cerezas:', font, self.WHITE)

        aler_number = Alert('Ingresa un valor valido.',font_subtittle, (255,0,0), self.WHITE, 1000, self.HEIGHT//2, 3000)
        aler_cant = Alert('El valor supera el maximo "9".',font_subtittle, (255,0,0), self.WHITE, 1000, self.HEIGHT//2, 3000)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_home.is_clicked():
                        running = False
                    elif button_dijkstra.is_clicked():
                        try:
                            int_value_ghost =  int (value_ghots.information_text())
                            int_value_cherryry = int (value_cherry.information_text())
                            int_value_pill = int(value_pill.information_text())
                            if int_value_cherryry < 9 and int_value_cherryry > 0 and int_value_ghost < 9 and int_value_ghost > 0 and int_value_pill < 9 and int_value_pill > 0:
                                self.grid = self.generate_new_grid(int_value_ghost, int_value_cherryry, int_value_pill)
                                visible_path_dijkstra = True
                            else:
                                aler_cant.tiempo_mostrado = pygame.time.get_ticks()
                                aler_cant.mostrar_alerta = True 
                        except ValueError:
                            aler_number.tiempo_mostrado = pygame.time.get_ticks()
                            aler_number.mostrar_alerta = True 
                    elif click_area.collidepoint(event.pos):
                        webbrowser.open(url)
                value_ghots.handle_event(event)
                value_cherry.handle_event(event)
                value_pill.handle_event(event)

            value_ghots.update()
            value_cherry.update()
            value_pill.update()

            self.screen.blit(fondo, (0,0))
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0, 1350-25, 800, 25))
            self.screen.blit(icon_git, (610, 775))
            text_git.draw(self.screen)
            button_home.draw(self.screen)

            value_ghots.draw(self.screen)
            value_cherry.draw(self.screen)
            value_pill.draw(self.screen)

            button_dijkstra.draw(self.screen)

            text_number_cherry.draw(self.screen)
            text_number_ghost.draw(self.screen)
            text_number_pill.draw(self.screen)

            aler_cant.draw(self.screen)
            aler_number.draw(self.screen)

            if visible_path_dijkstra is False:
                self.draw_board()
            elif visible_path_dijkstra is True:
                self.draw_board_path_dijkstra()
            pygame.display.update()
        



