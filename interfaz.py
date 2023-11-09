import pygame
import webbrowser
import math
from button import Button
from text_box import TextBox
from text import Text
from binary_tree import BinaryTree
from nary_tree import NaryTree
from checkbox import Checkbox

pygame.init()
screen = pygame.display.set_mode((1350, 800))
screen_width = 1350
screen_height = 800
button_width = 148
button_height = 47
button_x = (screen_width - button_width) // 2 #Centrar button
pygame.display.set_caption("Final project")
fondo = pygame.image.load('images/fondo.jpg')
button_home = Button(1305, 730, 'images/home.jpeg', '', 0, (0,0,0), (0,0,0))

binary_treee = BinaryTree()
nary_treee = NaryTree()

icon_git = pygame.image.load('images/git.jpg')
font_git = pygame.font.Font(None, 25)
text_git = Text(screen_width/2, 781, 'juancampos012', font_git, (0,0,0))
click_area = pygame.Rect(0, screen_height-25, screen_width, 25)
url = 'https://github.com/juancampos012/final_project_python'

BLACK = (0,0,0)
WHITE = (255, 255, 255)

def principal():
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

        screen.blit(fondo, (0,0))
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))
        screen.blit(icon_git, (610, 775))
        text_git.draw(screen)
        text_tittle.draw(screen)
        button_menu.draw(screen)
        button_grafos.draw(screen)
        if active_desplegable_tree is True:
            button_binary_tree.draw(screen)
            button_n_tree.draw(screen)
            if button_binary_tree.is_clicked():
                binary_tree()
            elif button_n_tree.is_clicked():
                tree_nario()
        elif active_desplegable_grafo is True:
            button_dijkstra.draw(screen)
        pygame.display.update()

def binary_tree():
    visible_tree = False
    visible_checkbox = False
    visible_traverse_inorder = False
    visible_traverse_preorder = False
    visible_traverse_postorder = False
    visible_traverse_level = False
    traverse_tree = []

    font = pygame.font.Font(None, 20)
    font_tittle = pygame.font.Font(None,35)
    font_subtittle = pygame.font.Font(None, 25)
    font_subtittle2 = pygame.font.Font(None, 30)
    text_color = BLACK
    input_color = WHITE
    cursor_color = BLACK

    button_create_binary_tree = Button(190, 215, 'images/buttonf.jpeg', 'Generar Arbol', 27, WHITE, (220,220,220))

    numbers_nodes = TextBox(165, 75, 300, 20, font, text_color, input_color, cursor_color)
    values = TextBox(165, 125, 300, 20, font, text_color, input_color, cursor_color)
    value_root = TextBox(165, 175, 300, 20, font, text_color, input_color, cursor_color)

    text_tittle = Text(168, 25, 'Arboles binarios.', font_tittle, text_color)
    text1 = Text(20, 78, "Cantidad de nodos:", font, text_color)
    text2 = Text(20, 128, "valores:", font, text_color)
    text3 = Text(20, 173, "Raiz:", font, text_color)
    text_profundidad = Text(20, 400, '-Profundidad', font_subtittle, text_color)
    text_amplitude = Text(20, 370, '-Amplitud', font_subtittle, text_color)
    text_recorrido = Text(20, 330, 'Recorrido', font_subtittle2, text_color)
    text_values_traverse = Text(20, 550, '', font, text_color)

    checkbox_inorden = Checkbox(50, 430, 20, 20, "Inorden", font, BLACK)
    checkbox_preorden = Checkbox(50, 460, 20, 20, "Preorden", font, BLACK)
    checkbox_postorden = Checkbox(50, 490, 20, 20, "Postorden", font, BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if click_area.collidepoint(event.pos):
                    webbrowser.open(url)
                if button_home.is_clicked():
                    principal()
                elif button_create_binary_tree.is_clicked():
                    information_numbers_nodes = numbers_nodes.information_text()
                    information_values = values.information_text()
                    information_value_root= value_root.information_text()
                    separate_information_values = information_values.split(',')
                    try:
                        numbers_nodes_int = int(information_numbers_nodes) 
                        value_root_int = int(information_value_root)
                        if numbers_nodes_int != 1:
                            separate_values = [int(x) for x in separate_information_values]
                            if numbers_nodes_int <= 20 and numbers_nodes_int > 0:
                                if numbers_nodes_int-1 ==  len(separate_values):
                                    aux = create_binary_tree(value_root_int, separate_values)
                                    if aux == True:
                                        print('No se pudo crear el arbol, no puede tener valores repetidos')
                                        binary_treee.delete_tree()
                                    if visible_tree == True:
                                        binary_treee.delete_tree()
                                        visible_tree = False
                                    else:
                                        visible_tree = True
                                else:
                                    print('Cantidad de nodos no coincide con los nodos ingresados')
                            else:
                                print('Cantidad de nodos no valida')
                        elif numbers_nodes_int == 1:
                            create_binary_tree_one_node(value_root_int)
                    except ValueError:
                        print('Ingresa valores validos')
                if text_amplitude.clicked_on_text(event.pos) == True:
                    traverse_tree = binary_treee.traverse_level_order()
                    numbers = ', '.join(map(str, traverse_tree))
                    text_values_traverse.set_text(numbers)
                    visible_traverse_level = True
                if text_profundidad.clicked_on_text(event.pos) == True and visible_checkbox == False:
                    visible_checkbox = True
                elif text_profundidad.clicked_on_text(event.pos) == True and visible_checkbox == True:
                    visible_checkbox = False
                if visible_checkbox == True:
                    checkbox_inorden.handle_event(event)
                    checkbox_postorden.handle_event(event)
                    checkbox_preorden.handle_event(event)
                    if checkbox_inorden.checked == True:
                        checkbox_preorden.checked = False
                        checkbox_postorden.checked = False
                        traverse_tree = binary_treee.traverse_inorder()
                        numbers = ', '.join(map(str, traverse_tree))
                        text_values_traverse.set_text(numbers)
                        visible_traverse_inorder = True
                    elif checkbox_preorden.checked == True:
                        checkbox_inorden.checked = False
                        checkbox_postorden.checked = False
                        traverse_tree = binary_treee.traverse_preorder()
                        numbers = ', '.join(map(str, traverse_tree))
                        text_values_traverse.set_text(numbers)
                        visible_traverse_preorder = True
                    elif checkbox_postorden.checked == True:
                        checkbox_inorden.checked = False
                        checkbox_preorden.checked = False
                        traverse_tree = binary_treee.traverse_postorder()
                        numbers = ', '.join(map(str, traverse_tree))
                        text_values_traverse.set_text(numbers)
                        visible_traverse_postorder = True
                    if checkbox_postorden.checked == False:
                        visible_traverse_postorder = False
                        visible_traverse_level = False
                    if checkbox_inorden.checked == False:
                        visible_traverse_inorder = False
                        visible_traverse_level = False
                    if checkbox_preorden.checked == False:
                        visible_traverse_preorder = False
                        visible_traverse_level = False
            numbers_nodes.handle_event(event)
            values.handle_event(event)
            value_root.handle_event(event)

        numbers_nodes.update()
        values.update()
        value_root.update()

        screen.blit(fondo, (0,0))
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))
        screen.blit(icon_git, (610, 775))
        text_git.draw(screen)

        numbers_nodes.draw(screen)
        values.draw(screen)
        value_root.draw(screen)

        text_tittle.draw(screen)
        text1.draw(screen)
        text2.draw(screen)
        text3.draw(screen)
        text_profundidad.draw(screen)
        text_amplitude.draw(screen)
        text_recorrido.draw(screen)

        button_create_binary_tree.draw(screen)
        button_home.draw(screen)

        draw_tree(binary_treee.root, 900, 50, 1, 800 // 2, 15)
        if visible_checkbox == True:
            checkbox_preorden.draw(screen)
            checkbox_inorden.draw(screen)
            checkbox_postorden.draw(screen)
        if visible_traverse_postorder == True or visible_traverse_inorder == True or visible_traverse_preorder == True or visible_traverse_level == True:
            text_values_traverse.draw(screen)
        pygame.display.update()

def tree_nario():
    visible_tree = False
    visible_checkbox = False
    visible_traverse_inorder = False
    visible_traverse_preorder = False
    visible_traverse_postorder = False
    visible_traverse_level = False

    font = pygame.font.Font(None, 20)
    font_tittle = pygame.font.Font(None,35)
    font_subtittle = pygame.font.Font(None, 25)
    font_subtittle2 = pygame.font.Font(None, 30)

    text_color = BLACK
    input_color = WHITE
    cursor_color = BLACK

    value_root = TextBox(165, 75, 300, 20, font, text_color, input_color, cursor_color)
    value_parent = TextBox(165, 125, 300, 20, font, text_color, input_color, cursor_color)
    value_node = TextBox(165, 175, 300, 20, font, text_color, input_color, cursor_color)

    text_tittle = Text(168, 25, 'Arboles n-arios.', font_tittle, text_color)
    text_value_root= Text(20, 78, "valor de la raiz:", font, text_color)
    text_value_parent = Text(20, 128, "Valor nodo padre:", font, text_color)
    text_value_node = Text(20, 173, "Valor nodo:", font, text_color)
    text_profundidad = Text(20, 400, '-Profundidad', font_subtittle, text_color)
    text_amplitude = Text(20, 370, '-Amplitud', font_subtittle, text_color)
    text_recorrido = Text(20, 330, 'Recorrido', font_subtittle2, text_color)
    text_values_traverse = Text(20, 550, '', font, text_color)

    checkbox_inorden = Checkbox(50, 430, 20, 20, "Inorden", font, BLACK)
    checkbox_preorden = Checkbox(50, 460, 20, 20, "Preorden", font, BLACK)
    checkbox_postorden = Checkbox(50, 490, 20, 20, "Postorden", font, BLACK)

    button_paint_tree = Button(155, 215, 'images/buttonf.jpeg', 'Pintar arbol', 27, WHITE, (220,220,220))
    button_add_node = Button(325, 215, 'images/buttonf.jpeg', 'Anadir nodo', 27, WHITE, (220,220,220))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_home.is_clicked():
                    principal()
                if click_area.collidepoint(event.pos):
                    webbrowser.open(url)
                if button_paint_tree.is_clicked():
                    visible_tree = True
                if button_add_node.is_clicked():
                    try:
                        if nary_treee.root == None:
                            nary_treee.add_root(int(value_root.information_text()))
                        else:
                            nary_treee.add_node(int(value_node.information_text()), int(value_parent.information_text()))
                    except ValueError:
                        print('Valor invalido') 
                if text_amplitude.clicked_on_text(event.pos) == True:
                    traverse_tree = nary_treee.level_order()
                    numbers = ', '.join(map(str, traverse_tree))
                    text_values_traverse.set_text(numbers)
                    visible_traverse_level = True
                if text_profundidad.clicked_on_text(event.pos) == True and visible_checkbox == False:
                    visible_checkbox = True
                elif text_profundidad.clicked_on_text(event.pos) == True and visible_checkbox == True:
                    visible_checkbox = False
                if visible_checkbox == True:
                    checkbox_inorden.handle_event(event)
                    checkbox_postorden.handle_event(event)
                    checkbox_preorden.handle_event(event)
                    if checkbox_inorden.checked == True:
                        checkbox_preorden.checked = False
                        checkbox_postorden.checked = False
                        traverse_tree = nary_treee.inorder()
                        numbers = ', '.join(map(str, traverse_tree))
                        text_values_traverse.set_text(numbers)
                        visible_traverse_inorder = True
                    elif checkbox_preorden.checked == True:
                        checkbox_inorden.checked = False
                        checkbox_postorden.checked = False
                        traverse_tree = nary_treee.preorder()
                        numbers = ', '.join(map(str, traverse_tree))
                        text_values_traverse.set_text(numbers)
                        visible_traverse_preorder = True
                    elif checkbox_postorden.checked == True:
                        checkbox_inorden.checked = False
                        checkbox_preorden.checked = False
                        traverse_tree = nary_treee.postorder()
                        numbers = ', '.join(map(str, traverse_tree))
                        text_values_traverse.set_text(numbers)
                        visible_traverse_postorder = True
                    if checkbox_postorden.checked == False:
                        visible_traverse_postorder = False
                        visible_traverse_level = False
                    if checkbox_inorden.checked == False:
                        visible_traverse_inorder = False
                        visible_traverse_level = False
                    if checkbox_preorden.checked == False:
                        visible_traverse_preorder = False
                        visible_traverse_level = False
            value_root.handle_event(event)
            value_parent.handle_event(event)
            value_node.handle_event(event)

        value_node.update()
        value_parent.update()
        value_root.update()

        screen.blit(fondo, (0,0))
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, screen_height-25, screen_width, 25))

        button_home.draw(screen)
        button_paint_tree.draw(screen)
        button_add_node.draw(screen)

        text_tittle.draw(screen)
        text_value_parent.draw(screen)
        text_value_node.draw(screen)
        text_value_root.draw(screen)
        text_profundidad.draw(screen)
        text_amplitude.draw(screen)
        text_recorrido.draw(screen)

        value_root.draw(screen)
        value_parent.draw(screen)
        value_node.draw(screen)

        screen.blit(icon_git, (610, 775))
        text_git.draw(screen)

        if visible_tree == True:
            draw_ntree(nary_treee.root, 900, 50, 800, screen, 15)
        if visible_checkbox == True:
            checkbox_preorden.draw(screen)
            checkbox_inorden.draw(screen)
            checkbox_postorden.draw(screen)
        
        if visible_traverse_level is True or visible_traverse_postorder is True or visible_traverse_preorder is True or visible_traverse_inorder is True:
            text_values_traverse.draw(screen)
        pygame.display.update()

def create_binary_tree_one_node(value_root):
    binary_treee.insert(value_root)

def create_binary_tree(value_root, values_nodes):
    binary_treee.insert(value_root)
    aux = False
    if len(values_nodes) > 0:
        for i in range(0, len(values_nodes)):
            aux = binary_treee.insert(values_nodes[i])
            if aux is True:
                return True

def draw_arrow_line(screen, color, start, end, arrow_size):
    pygame.draw.line(screen, color, start, end)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    pygame.draw.polygon(screen, color, (
        (end[0] - arrow_size * math.cos(angle - math.pi / 6), end[1] - arrow_size * math.sin(angle - math.pi / 6)),
        (end[0] - arrow_size * math.cos(angle + math.pi / 6), end[1] - arrow_size * math.sin(angle + math.pi / 6)),
        (end[0], end[1])
    ))

def draw_tree(node, x, y, level, width, aux):
    if node is not None:
        pygame.draw.circle(screen, BLACK, (x, y), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(node.value), True, WHITE)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
        if node.left is not None:
            next_y = y + 100
            draw_arrow_line(screen, BLACK, (x, y + 20), ((x - width // 2)+aux, next_y-18), 10)
            draw_tree(node.left, x - width // 2, next_y, level + 1, width // 2, aux-2)

        if node.right is not None:
            next_y = y + 100
            draw_arrow_line(screen, BLACK, (x, y + 20), ((x + width // 2)-aux, next_y-18), 10)
            draw_tree(node.right, x + width // 2, next_y, level + 1, width // 2, aux-2)

def draw_ntree(node, x, y, width, screen, aux):
    # Dibuja el nodo actual
    pygame.draw.circle(screen, BLACK, (x, y), 20)
    font = pygame.font.Font(None, 36)
    text = font.render(str(node.value), True, WHITE)
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
        draw_arrow_line(screen, BLACK, (x, y + 20), (child_x, child_y-23), 10)
        draw_ntree(child, child_x, child_y, child_width, screen, aux)
        child_x += child_width

principal()