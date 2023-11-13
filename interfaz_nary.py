import pygame
import webbrowser
import math
from button import Button
from text_box import TextBox
from text import Text
from nary_tree import NaryTree
from checkbox import Checkbox
from alert import Alert

class InterfazNary: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1350, 800))  
        self.BLACK = (0,0,0)
        self.WHITE = (255, 255, 255)
        self.nary_treee = NaryTree()

    def nario_tree(self):
        screen_width = 1350
        screen_height = 800
        pygame.display.set_caption("Final project")
        fondo = pygame.image.load('images/fondo.jpg')
        button_home = Button(1305, 730, 'images/home.jpeg', '', 0, (0,0,0), (0,0,0))

        icon_git = pygame.image.load('images/git.jpg')
        font_git = pygame.font.Font(None, 25)
        text_git = Text(screen_width/2, 781, 'juancampos012', font_git, self.BLACK)
        click_area = pygame.Rect(0, screen_height-25, screen_width, 25)
        url = 'https://github.com/juancampos012/final_project_python'

        visible_tree = False
        visible_checkbox = False
        visible_traverse_preorder = False
        visible_traverse_postorder = False
        visible_traverse_level = False

        font = pygame.font.Font(None, 20)
        font_tittle = pygame.font.Font(None,35)
        font_subtittle = pygame.font.Font(None, 25)
        font_subtittle2 = pygame.font.Font(None, 30)

        text_color = self.BLACK
        input_color = self.WHITE
        cursor_color = self.BLACK

        value_root = TextBox(165, 75, 300, 20, font, text_color, input_color, cursor_color)
        value_level = TextBox(165, 125, 300, 20, font, text_color, input_color, cursor_color)
        value_position = TextBox(165, 175, 300, 20, font, text_color, input_color, cursor_color)
        value_node = TextBox(165, 225, 300, 20, font, text_color, input_color, cursor_color)

        text_tittle = Text(168, 25, 'Arboles n-arios.', font_tittle, text_color)
        text_value_root= Text(20, 78, "valor de la raiz:", font, text_color)
        text_value_level = Text(20, 128, "Nivel:", font, text_color)
        text_value_position = Text(20, 178, "Poscion:", font, text_color)
        text_value_node = Text(20, 228, "Valor nodo:", font, text_color)
        text_profundidad = Text(20, 400, '-Profundidad', font_subtittle, text_color)
        text_amplitude = Text(20, 370, '-Amplitud', font_subtittle, text_color)
        text_recorrido = Text(20, 330, 'Recorrido', font_subtittle2, text_color)
        text_values_traverse = Text(20, 550, '', font, text_color)

        checkbox_preorden = Checkbox(50, 430, 20, 20, "Preorden", font, self.BLACK)
        checkbox_postorden = Checkbox(50, 460, 20, 20, "Postorden", font, self.BLACK)

        button_add_node = Button(190, 265, 'images/buttonf.jpeg', 'Anadir nodo', 27, self.WHITE, (220,220,220))

        alert_values_r = Alert('Los campos diferentes de la raiz deben de estar vacios.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_root_value = Alert('Ingresa un valor valido para la raiz.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_values = Alert('Ingresa valores validos.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_position = Alert('Posicion no econntrada.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_home.is_clicked():
                        running = False
                        visible_tree = False
                        self.nary_treee.delete_nary_tree()
                    elif click_area.collidepoint(event.pos):
                        webbrowser.open(url)
                    elif button_add_node.is_clicked():
                        if self.nary_treee.root == None:
                            if not value_level.information_text() and not value_position.information_text() and not value_node.information_text():
                                try: 
                                    self.nary_treee.add_root(int(value_root.information_text()))
                                    visible_tree = True
                                except ValueError:
                                    alert_root_value.tiempo_mostrado = pygame.time.get_ticks()
                                    alert_root_value.mostrar_alerta = True
                            else:
                                alert_values_r.tiempo_mostrado = pygame.time.get_ticks()
                                alert_values_r.mostrar_alerta = True 
                        else:
                            try:
                                aux = self.nary_treee.add_node(int(value_level.information_text()), int(value_position.information_text()), int(value_node.information_text()))
                                if aux is True:
                                    visible_tree = True
                                else:
                                    alert_position.tiempo_mostrado = pygame.time.get_ticks()
                                    alert_position.mostrar_alerta = True
                            except ValueError:
                                alert_values.tiempo_mostrado = pygame.time.get_ticks()
                                alert_values.mostrar_alerta = True
                    if text_amplitude.clicked_on_text(event.pos) == True and self.nary_treee.root is not None:
                        traverse_tree = self.nary_treee.level_order()
                        numbers = ', '.join(map(str, traverse_tree))
                        text_values_traverse.set_text(numbers)
                        visible_traverse_level = True
                    if text_profundidad.clicked_on_text(event.pos) == True and visible_checkbox == False:
                        visible_checkbox = True
                    elif text_profundidad.clicked_on_text(event.pos) == True and visible_checkbox == True:
                        visible_checkbox = False
                    if visible_checkbox == True and self.nary_treee.root is not None:
                        checkbox_postorden.handle_event(event)
                        checkbox_preorden.handle_event(event)
                        if checkbox_preorden.checked == True:
                            checkbox_postorden.checked = False
                            traverse_tree = self.nary_treee.preorder()
                            numbers = ', '.join(map(str, traverse_tree))
                            text_values_traverse.set_text(numbers)
                            visible_traverse_preorder = True
                        elif checkbox_postorden.checked == True:
                            checkbox_preorden.checked = False
                            traverse_tree = self.nary_treee.postorder()
                            numbers = ', '.join(map(str, traverse_tree))
                            text_values_traverse.set_text(numbers)
                            visible_traverse_postorder = True
                        if checkbox_postorden.checked == False:
                            visible_traverse_postorder = False
                            visible_traverse_level = False
                        if checkbox_preorden.checked == False:
                            visible_traverse_preorder = False
                            visible_traverse_level = False
                value_root.handle_event(event)
                value_level.handle_event(event)
                value_node.handle_event(event)
                value_position.handle_event(event)

            value_node.update()
            value_position.update()
            value_root.update()
            value_level.update()

            self.screen.blit(fondo, (0,0))
            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))

            button_home.draw(self.screen)
            button_add_node.draw(self.screen)

            text_tittle.draw(self.screen)
            text_value_level.draw(self.screen)
            text_value_position.draw(self.screen)
            text_value_node.draw(self.screen)
            text_value_root.draw(self.screen)
            text_profundidad.draw(self.screen)
            text_amplitude.draw(self.screen)
            text_recorrido.draw(self.screen)

            value_root.draw(self.screen)
            value_level.draw(self.screen)
            value_node.draw(self.screen)
            value_position.draw(self.screen)

            self.screen.blit(icon_git, (610, 775))
            text_git.draw(self.screen)

            alert_values_r.draw(self.screen)
            alert_root_value.draw(self.screen)
            alert_values.draw(self.screen)
            alert_position.draw(self.screen)

            if visible_tree == True:
                self.draw_ntree(self.nary_treee.root, 900, 50, 800, self.screen, 15)
            if visible_checkbox == True:
                checkbox_preorden.draw(self.screen)
                checkbox_postorden.draw(self.screen)
            
            if visible_traverse_level is True or visible_traverse_postorder is True or visible_traverse_preorder is True:
                text_values_traverse.draw(self.screen)
            pygame.display.update()

    def draw_arrow_line(self, screen, color, start, end, arrow_size):
        pygame.draw.line(screen, color, start, end)
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        pygame.draw.polygon(screen, color, (
            (end[0] - arrow_size * math.cos(angle - math.pi / 6), end[1] - arrow_size * math.sin(angle - math.pi / 6)),
            (end[0] - arrow_size * math.cos(angle + math.pi / 6), end[1] - arrow_size * math.sin(angle + math.pi / 6)),
            (end[0], end[1])
        ))
    
    def draw_ntree(self, node, x, y, width, screen, aux):
        # Dibuja el nodo actual
        pygame.draw.circle(screen, self.BLACK, (x, y), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(node.value), True, self.WHITE)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

        # Calcula la posición de los hijos
        num_children = len(node.children)
        if num_children == 0:
            child_width = width
        else:
            child_width = width / num_children
        child_x = x - width / 2 + child_width / 2
        child_y = y + 100

        # Dibuja los hijos
        for child in node.children:
            self.draw_arrow_line(screen, self.BLACK, (x, y + 20), (child_x, child_y-23), 10)
            self.draw_ntree(child, child_x, child_y, child_width, screen, aux)
            child_x += child_width