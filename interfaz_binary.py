import pygame
import webbrowser
import math
from button import Button
from text_box import TextBox
from text import Text
from binary_tree import BinaryTree
from checkbox import Checkbox
from alert  import Alert

class InterfazBinary:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1350, 800))  
        self.BLACK = (0,0,0)
        self.WHITE = (255, 255, 255)
        self.binary_treee = BinaryTree()

    def binary_tree(self):
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
        visible_traverse_amplitud = False
        visible_traverse_inorden = False
        visible_traverse_preorden = False
        visible_traverse_postorden = False

        font = pygame.font.Font(None, 20)
        font_tittle = pygame.font.Font(None,35)
        font_subtittle = pygame.font.Font(None, 25)
        font_subtittle2 = pygame.font.Font(None, 30)
        text_color = self.BLACK
        input_color = self.WHITE
        cursor_color = self.BLACK

        button_create_binary_tree = Button(70, 265, 'images/buttonf.jpeg', 'Generar Arbol', 27, self.WHITE, (220,220,220))
        button_delete_node = Button(240, 265, 'images/buttonf.jpeg', 'Eliminar nodo', 27, self.WHITE, (220,220,220))

        numbers_nodes = TextBox(165, 75, 300, 20, font, text_color, input_color, cursor_color)
        values = TextBox(165, 125, 300, 20, font, text_color, input_color, cursor_color)
        value_root = TextBox(165, 175, 300, 20, font, text_color, input_color, cursor_color)
        value_node_delete = TextBox(165, 225, 300, 20, font, text_color, input_color, cursor_color)

        text_tittle = Text(168, 25, 'Arboles binarios.', font_tittle, text_color)
        text1 = Text(20, 78, "Cantidad de nodos:", font, text_color)
        text2 = Text(20, 128, "valores:", font, text_color)
        text3 = Text(20, 178, "Raiz:", font, text_color)
        text_profundidad = Text(20, 430, '-Profundidad', font_subtittle, text_color)
        text_amplitude = Text(20, 380, '-Amplitud', font_subtittle, text_color)
        text_recorrido = Text(20, 350, 'Recorrido', font_subtittle2, text_color)
        text_values_traverse_amplitud = Text(20, 560, '', font, text_color)
        text_values_traverse_inorden = Text(20, 590, '', font, text_color)
        text_values_traverse_preorden = Text(20, 620, '', font, text_color)
        text_values_traverse_postorden = Text(20, 650, '', font, text_color)
        text_value_delete = Text(20, 228, 'Valor nodo eliminar:', font, text_color)

        checkbox_inorden = Checkbox(50, 460, 20, 20, "Inorden", font, self.BLACK)
        checkbox_preorden = Checkbox(50, 490, 20, 20, "Preorden", font, self.BLACK)
        checkbox_postorden = Checkbox(50, 520, 20, 20, "Postorden", font, self.BLACK)
        checkbox_amplitud = Checkbox(50, 405, 20, 20, "Amplitud", font, self.BLACK)

        alert_cant_numbers = Alert('', font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_root = Alert('Ingresa un valor valido para la raiz.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_number_nodes = Alert('Ingresa un numero de nodos valido.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_cant_ivalid = Alert('Cantidad de nodos no esta dentro del limite 0-20.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_only_root = Alert('Quita los valores de la casilla de valores.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_repeat_number = Alert('No pueden haber numeros repetidos.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)
        alert_negative_number = Alert('No pueden haber numeros negativos.',font_subtittle, (255,0,0), self.WHITE, screen_width//2, screen_height//2, 3000)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if click_area.collidepoint(event.pos):
                        webbrowser.open(url)
                    if button_home.is_clicked():
                        running = False
                        self.binary_treee.delete_tree()
                    elif button_delete_node.is_clicked():
                        try:
                            value_node_delete_int = int(value_node_delete.information_text())
                            self.binary_treee.delete_node_recursive(value_node_delete_int)
                            visible_tree = True
                        except ValueError:
                            alert_number_nodes.tiempo_mostrado = pygame.time.get_ticks()
                            alert_number_nodes.mostrar_alerta = True 
                    elif button_create_binary_tree.is_clicked():
                        information_numbers_nodes = numbers_nodes.information_text()
                        information_values = values.information_text()
                        information_value_root= value_root.information_text()
                        separate_information_values = information_values.split(',')
                        try:
                            value_root_int = int(information_value_root)
                            try:
                                numbers_nodes_int = int(information_numbers_nodes) 
                                if numbers_nodes_int != 1:
                                    separate_values = [int(x) for x in separate_information_values]
                                    separate_values_all = self.eliminar_repetidos(separate_values)
                                    if numbers_nodes_int <= 20 and numbers_nodes_int > 0:
                                        if all(num > 0 for num in separate_values_all) and value_root_int > 0:
                                            if numbers_nodes_int - 1 ==  len(separate_values_all):
                                                self.create_binary_tree(value_root_int, separate_values_all)
                                                if visible_tree == True:
                                                    self.binary_treee.delete_tree()
                                                    visible_tree = False
                                                else:
                                                    visible_tree = True
                                            else:
                                                aux = len(separate_values_all) - numbers_nodes_int + 1
                                                aux_text = 'Cantidadad de nodos esta incorrecta por '+str(aux)+' valores'
                                                alert_cant_numbers.mensaje = aux_text
                                                alert_cant_numbers.tiempo_mostrado = pygame.time.get_ticks()
                                                alert_cant_numbers.mostrar_alerta = True 
                                        else:
                                            alert_negative_number.tiempo_mostrado = pygame.time.get_ticks()
                                            alert_negative_number.mostrar_alerta = True
                                    else:
                                        alert_cant_ivalid.tiempo_mostrado = pygame.time.get_ticks()
                                        alert_cant_ivalid.mostrar_alerta = True 
                                elif numbers_nodes_int == 1:
                                    information_values = values.information_text()
                                    if not information_values:
                                        if value_root_int > 0:
                                            self.create_binary_tree_one_node(value_root_int)
                                            if visible_tree == True:
                                                self.binary_treee.delete_tree()
                                                visible_tree = False
                                            else:
                                                visible_tree = True
                                        else:
                                            alert_negative_number.tiempo_mostrado = pygame.time.get_ticks()
                                            alert_negative_number.mostrar_alerta = True
                                    else:
                                        alert_only_root.tiempo_mostrado = pygame.time.get_ticks()
                                        alert_only_root.mostrar_alerta = True
                            except ValueError:
                                alert_number_nodes.tiempo_mostrado = pygame.time.get_ticks()
                                alert_number_nodes.mostrar_alerta = True 
                        except ValueError:
                            alert_root.tiempo_mostrado = pygame.time.get_ticks()
                            alert_root.mostrar_alerta = True 
                    if visible_tree is True:
                        checkbox_amplitud.handle_event(event)
                        checkbox_inorden.handle_event(event)
                        checkbox_postorden.handle_event(event)
                        checkbox_preorden.handle_event(event)
                if checkbox_amplitud.checked is True and self.binary_treee.root is not None:
                    traverse_tree = self.binary_treee.traverse_level_order()
                    numbers = 'Amplitud: '+', '.join(map(str, traverse_tree))
                    text_values_traverse_amplitud.set_text(numbers)
                    visible_traverse_amplitud = True
                else:
                    visible_traverse_amplitud = False
                if checkbox_inorden.checked is True and self.binary_treee.root is not None:
                    traverse_tree = self.binary_treee.traverse_inorder()
                    numbers = 'Inorden: '+', '.join(map(str, traverse_tree))
                    text_values_traverse_inorden.set_text(numbers)
                    visible_traverse_inorden = True
                else:
                    visible_traverse_inorden = False
                if checkbox_postorden.checked is True and self.binary_treee.root is not None:
                    traverse_tree = self.binary_treee.traverse_postorder()
                    numbers = 'Postorden: '+', '.join(map(str, traverse_tree))
                    text_values_traverse_postorden.set_text(numbers)
                    visible_traverse_postorden = True
                else:
                    visible_traverse_postorden = False
                if checkbox_preorden.checked is True and self.binary_treee.root is not None:
                    traverse_tree = self.binary_treee.traverse_preorder()
                    numbers = 'Preorden: '+', '.join(map(str, traverse_tree))
                    text_values_traverse_preorden.set_text(numbers)
                    visible_traverse_preorden = True
                else:
                    visible_traverse_preorden = False
                numbers_nodes.handle_event(event)
                values.handle_event(event)
                value_root.handle_event(event)
                value_node_delete.handle_event(event)

            numbers_nodes.update()
            values.update()
            value_root.update()
            value_node_delete.update()

            self.screen.blit(fondo, (0,0))
            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))
            self.screen.blit(icon_git, (610, 775))
            text_git.draw(self.screen)

            numbers_nodes.draw(self.screen)
            values.draw(self.screen)
            value_root.draw(self.screen)
            value_node_delete.draw(self.screen)

            text_tittle.draw(self.screen)
            text1.draw(self.screen)
            text2.draw(self.screen)
            text3.draw(self.screen)
            text_profundidad.draw(self.screen)
            text_amplitude.draw(self.screen)
            text_recorrido.draw(self.screen)
            text_value_delete.draw(self.screen)

            button_create_binary_tree.draw(self.screen)
            button_home.draw(self.screen)
            button_delete_node.draw(self.screen)

            self.draw_tree(self.binary_treee.root, 900, 50, 1, 800 // 2, 15)
            checkbox_preorden.draw(self.screen)
            checkbox_inorden.draw(self.screen)
            checkbox_postorden.draw(self.screen)

            checkbox_amplitud.draw(self.screen)
            alert_cant_numbers.draw(self.screen)
            alert_number_nodes.draw(self.screen)
            alert_root.draw(self.screen)
            alert_cant_ivalid.draw(self.screen)
            alert_repeat_number.draw(self.screen)
            alert_negative_number.draw(self.screen)
            alert_only_root.draw(self.screen)

            if visible_traverse_amplitud == True:
                text_values_traverse_amplitud.draw(self.screen)
            if visible_traverse_inorden == True:
                text_values_traverse_inorden.draw(self.screen)
            if visible_traverse_postorden == True:
                text_values_traverse_postorden.draw(self.screen)
            if visible_traverse_preorden == True:
                text_values_traverse_preorden.draw(self.screen)
            pygame.display.update()

    def create_binary_tree_one_node(self, value_root):
        self.binary_treee.insert(value_root)

    def create_binary_tree(self, value_root, values_nodes):
        self.binary_treee.insert(value_root)
        aux = False
        if len(values_nodes) > 0:
            for i in range(0, len(values_nodes)):
                aux = self.binary_treee.insert(values_nodes[i])
                if aux is True:
                    return True
    
    def draw_arrow_line(self, screen, color, start, end, arrow_size):
        pygame.draw.line(screen, color, start, end)
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        pygame.draw.polygon(screen, color, (
            (end[0] - arrow_size * math.cos(angle - math.pi / 6), end[1] - arrow_size * math.sin(angle - math.pi / 6)),
            (end[0] - arrow_size * math.cos(angle + math.pi / 6), end[1] - arrow_size * math.sin(angle + math.pi / 6)),
            (end[0], end[1])
        ))

    def draw_tree(self, node, x, y, level, width, aux):
        if node is not None:
            pygame.draw.circle(self.screen, self.BLACK, (x, y), 20)
            font = pygame.font.Font(None, 36)
            text = font.render(str(node.value), True, self.WHITE)
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)
            if node.left is not None:
                next_y = y + 100
                self.draw_arrow_line(self.screen, self.BLACK, (x, y + 20), ((x - width // 2)+aux, next_y-18), 10)
                self.draw_tree(node.left, x - width // 2, next_y, level + 1, width // 2, aux-2)

            if node.right is not None:
                next_y = y + 100
                self.draw_arrow_line(self.screen, self.BLACK, (x, y + 20), ((x + width // 2)-aux, next_y-18), 10)
                self.draw_tree(node.right, x + width // 2, next_y, level + 1, width // 2, aux-2)

    def eliminar_repetidos(self, lista):
        lista_sin_repetidos = []
        for elemento in lista:
            if elemento not in lista_sin_repetidos:
                lista_sin_repetidos.append(elemento)
        return lista_sin_repetidos
    
    def verificar_repetidos(self, lista, root):
        for i in lista:
            if i == root:
                return True