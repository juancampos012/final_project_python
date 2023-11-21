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
        visible_traverse_level = False

        font = pygame.font.Font(None, 20)
        font_tittle = pygame.font.Font(None,35)
        font_subtittle = pygame.font.Font(None, 25)
        font_subtittle2 = pygame.font.Font(None, 30)

        text_color = self.BLACK
        input_color = self.WHITE
        cursor_color = self.BLACK

        number_nodess = TextBox(165, 75, 300, 20, font, text_color, input_color, cursor_color)
        value_root = TextBox(165, 125, 300, 20, font, text_color, input_color, cursor_color)
        number_children = TextBox(165, 175, 300, 20, font, text_color, input_color, cursor_color)
        values_children = TextBox(165, 225, 300, 20, font, text_color, input_color, cursor_color)
        value_node_delete = TextBox(165, 275, 300, 20, font, text_color, input_color, cursor_color)
        value_node_delete_all = TextBox(165, 325, 300, 20, font, text_color, input_color, cursor_color)

        text_tittle = Text(168, 25, 'Arboles n-arios.', font_tittle, text_color)
        text_numbers_nodes= Text(20, 78, "Cantidad total:", font, text_color)
        text_value_root = Text(20, 128, "Valor raiz:", font, text_color)
        text_number_children = Text(20, 178, "Cantidad hijos", font, text_color)
        text__values_children = Text(20, 228, "Valor hijos:", font, text_color)
        text__value_node_delete = Text(20, 278, "Valor eliminar:", font, text_color)
        text__value_node_delete_all = Text(20, 328, "Valor eliminar todos:", font, text_color)
        text_amplitude = Text(20, 490, '-Amplitud', font_subtittle, text_color)
        text_recorrido = Text(20, 450, 'Recorrido', font_subtittle2, text_color)
        text_values_traverse = Text(20, 520, '', font, text_color)

        checkbox_level = Checkbox(40, 520, 20, 20, "Amplitud", font, self.BLACK)

        button_add_node = Button(20, 375, 'images/buttonf.jpeg', 'Anadir nodo', 27, self.WHITE, (220,220,220))
        button_delete_node = Button(180, 375, 'images/buttonf.jpeg', 'Eliminar nodo', 27, self.WHITE, (220,220,220))
        button_delete_node_all = Button(340, 375, 'images/buttonf.jpeg', 'Eliminar todos', 27, self.WHITE, (220,220,220))

        alert_positive_numbers = Alert('Solo se pueden ingresar numeros positivos.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_values = Alert('Ingresa valores validos.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_position = Alert('Posicion no econntrada.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_nary_tree = Alert('El arbol no puede estar vacio.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_number_node= Alert('Numero de nodos no valido.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_nsearch = Alert('Nodo no encontrado.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_negative_number = Alert('No pueden haber numeros negativos.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_max_num = Alert('' ,font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_cant_numbers = Alert('Cantidad de nodos no coinciden con los valores ingresados.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)

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
                    elif button_delete_node_all.is_clicked():
                        try:
                            value_node_delete_all_int = int(value_node_delete_all.information_text())
                            aux_boolean_delete_all = self.nary_treee.eliminar_nodo(value_node_delete_all_int)
                            if aux_boolean_delete_all is False:
                                alert_nsearch.tiempo_mostrado = pygame.time.get_ticks()
                                alert_nsearch.mostrar_alerta = True
                            while aux_boolean_delete_all:
                                aux_boolean_delete_all = self.nary_treee.eliminar_nodo(value_node_delete_all_int)
                        except ValueError:
                            alert_values.tiempo_mostrado = pygame.time.get_ticks()
                            alert_values.mostrar_alerta = True
                    elif button_delete_node.is_clicked():
                        try:
                            value_node_delete_int = int(value_node_delete.information_text())
                            aux_boolean_delete = self.nary_treee.eliminar_nodo(value_node_delete_int)
                            visible_tree = True
                            if aux_boolean_delete is False:
                                alert_nsearch.tiempo_mostrado = pygame.time.get_ticks()
                                alert_nsearch.mostrar_alerta = True
                        except ValueError:
                            alert_values.tiempo_mostrado = pygame.time.get_ticks()
                            alert_values.mostrar_alerta = True
                    elif button_add_node.is_clicked():
                        try:
                            number_nodes_int = int(number_nodess.information_text())
                            if number_nodes_int <= 20 and number_nodes_int > 1: 
                                root_int = int(value_root.information_text())
                                if root_int > 0:
                                    number_children_int = int(number_children.information_text())
                                    if number_children_int > 0 and number_children_int < 20:
                                        values_children_arr =  values_children.information_text().split(',')
                                        values_children_arr_int = [int(x) for x in values_children_arr]
                                        if number_children_int  == len(values_children_arr):
                                            auxx = number_children_int + self.nary_treee.length
                                            print(auxx, number_nodes_int)
                                            if auxx < number_nodes_int:
                                                if all(num > 0 for num in values_children_arr_int):
                                                    aux_bool = self.nary_treee.add_node(root_int, values_children_arr_int)
                                                    if aux_bool is False:
                                                        alert_nsearch.tiempo_mostrado = pygame.time.get_ticks()
                                                        alert_nsearch.mostrar_alerta = True
                                                    visible_tree = True
                                                else:
                                                    alert_negative_number.tiempo_mostrado = pygame.time.get_ticks()
                                                    alert_negative_number.mostrar_alerta = True
                                            else:
                                                aux = (auxx - number_nodes_int)+1
                                                aux_text = 'Cantidadad de nodos esta incorrecta por '+str(aux)+' valores'
                                                alert_max_num.mensaje = aux_text
                                                alert_max_num.tiempo_mostrado = pygame.time.get_ticks()
                                                alert_max_num.mostrar_alerta = True
                                    elif number_children_int == 0:
                                        root_int = int(value_root.information_text())
                                        arr = []
                                        if root_int > 0:
                                            self.nary_treee.add_node(root_int, arr)
                                            visible_tree = True
                                    else:
                                        alert_cant_numbers.tiempo_mostrado = pygame.time.get_ticks()
                                        alert_cant_numbers.mostrar_alerta = True
                                else:
                                    alert_positive_numbers.tiempo_mostrado = pygame.time.get_ticks()
                                    alert_positive_numbers.mostrar_alerta = True
                            elif number_nodes_int == 1:
                                root_int = int(value_root.information_text())
                                if root_int > 0:
                                    self.nary_treee.add_root(root_int)
                                    visible_tree = True
                            else:
                                alert_number_node.tiempo_mostrado = pygame.time.get_ticks()
                                alert_number_node.mostrar_alerta = True
                        except ValueError:
                            alert_values.tiempo_mostrado = pygame.time.get_ticks()
                            alert_values.mostrar_alerta = True
                if checkbox_level.checked is True and self.nary_treee.root is not None:
                    traverse_tree = self.nary_treee.level_order()
                    numbers = 'Recorrido: '+', '.join(map(str, traverse_tree))
                    text_values_traverse.set_text(numbers)
                    visible_traverse_level = True
                else:
                    visible_traverse_level = False

                if self.nary_treee.root is None:
                    number_nodess.handle_event(event)

                checkbox_level.handle_event(event)
                value_root.handle_event(event)
                number_children.handle_event(event)
                values_children.handle_event(event)
                value_node_delete.handle_event(event)
                value_node_delete_all.handle_event(event)

            value_root.update()
            number_children.update()
            values_children.update()
            value_node_delete.update()
            value_node_delete_all.update()

            self.screen.blit(fondo, (0,0))
            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))

            button_home.draw(self.screen)
            button_add_node.draw(self.screen)
            button_delete_node.draw(self.screen)
            button_delete_node_all.draw(self.screen)

            text_tittle.draw(self.screen)
            text__values_children.draw(self.screen)
            text_number_children.draw(self.screen)
            text_value_root.draw(self.screen)
            text_numbers_nodes.draw(self.screen)
            text_amplitude.draw(self.screen)
            text_recorrido.draw(self.screen)
            text__value_node_delete.draw(self.screen)
            text__value_node_delete_all.draw(self.screen)

            number_nodess.draw(self.screen)
            values_children.draw(self.screen)
            value_root.draw(self.screen)
            number_children.draw(self.screen)
            value_node_delete.draw(self.screen)
            value_node_delete_all.draw(self.screen)

            self.screen.blit(icon_git, (610, 775))
            text_git.draw(self.screen)

            alert_positive_numbers.draw(self.screen)
            alert_values.draw(self.screen)
            alert_position.draw(self.screen)
            alert_nary_tree.draw(self.screen)
            alert_number_node.draw(self.screen)
            alert_cant_numbers.draw(self.screen)
            alert_negative_number.draw(self.screen)
            alert_max_num.draw(self.screen)
            alert_nsearch.draw(self.screen)

            checkbox_level.draw(self.screen)

            if visible_tree is True:
                self.draw_ntree(self.nary_treee.root, 900, 50, 800, self.screen, 15)
            
            if visible_traverse_level is True:
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
        if node.value is not None:
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
            if child.value is not None:
                self.draw_arrow_line(screen, self.BLACK, (x, y + 20), (child_x, child_y-23), 10)
            self.draw_ntree(child, child_x, child_y, child_width, screen, aux)
            child_x += child_width