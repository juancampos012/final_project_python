import pygame
import webbrowser
from button import Button
from text_box import TextBox
from text import Text
from binary_tree import BinaryTree

pygame.init()
screen = pygame.display.set_mode((900, 725))
win_height = 450
win_width = 900
pygame.display.set_caption("Final project")
fondo = pygame.image.load('images/fondo.png')
button_home = Button(837, 637, 'images/home.jpeg', '', 0, (0,0,0), (0,0,0))
binary_treee = BinaryTree()

def principal():
    icon_git = pygame.image.load('images/git.jpg')
    button_menu = Button(367, 175, 'images/buttonf.jpeg', 'Arboles' , 40, (255,255,255), (220,220,220))
    button_binary_tree = Button(367, 225, 'images/buttonf.jpeg', 'Binarios', 40, (255,255,255), (220,220,220))
    button_n_tree = Button(367, 275, 'images/buttonf.jpeg', 'N-arios', 40, (255,255,255), (220,220,220))
    button_grafos = Button(367, 430, 'images/buttonf.jpeg', 'grafos', 40, (255,255,255), (220,220,220))
    button_dijkstra = Button(367, 480, 'images/buttonf.jpeg', 'Dijkstra', 40, (255,255,255), (220,220,220))
    font_tittle = pygame.font.Font(None,50)
    text_tittle = Text(300, 60, 'Menu de opciones.', font_tittle, (0,0,0))
    font_git = pygame.font.Font(None, 25)
    text_git = Text(430, 706, 'juancampos012', font_git, (0,0,0))
    click_area = pygame.Rect(0, 700, 900, 25)
    url = "https://github.com/juancampos012?tab=repositories"

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
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 700, 900, 25))
        screen.blit(icon_git, (370, 700))
        text_tittle.draw(screen)
        text_git.draw(screen)
        button_menu.draw(screen)
        button_grafos.draw(screen)
        if active_desplegable_tree is True:
            button_binary_tree.draw(screen)
            button_n_tree.draw(screen)
            if button_binary_tree.is_clicked():
                binary_tree()
        elif active_desplegable_grafo is True:
            button_dijkstra.draw(screen)
        pygame.display.update()

def binary_tree():
    visible_tree = False
    font = pygame.font.Font(None, 20)
    font_tittle = pygame.font.Font(None,35)
    text_color = (0, 0, 0)
    input_color = (250, 250, 250)
    cursor_color = (0, 0, 0)
    button_create_binary_tree = Button(380, 215, 'images/buttonf.jpeg', 'Generar Arbol', 27, (255,255,255), (220,220,220))

    numbers_nodes = TextBox(383, 75, 300, 20, font, text_color, input_color, cursor_color)
    values = TextBox(383, 125, 300, 20, font, text_color, input_color, cursor_color)
    value_root = TextBox(383, 175, 300, 20, font, text_color, input_color, cursor_color)

    text_tittle = Text(350, 25, 'Arboles binarios.', font_tittle, text_color)
    text1 = Text(240, 78, "Cantidad de nodos:", font, text_color)
    text2 = Text(240, 128, "valores:", font, text_color)
    text3 = Text(240, 173, "Raiz:", font, text_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                                    create_binary_tree(value_root_int, separate_values)
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
                        print('Vuelve a intentarlo')
            numbers_nodes.handle_event(event)
            values.handle_event(event)
            value_root.handle_event(event)

        numbers_nodes.update()
        values.update()
        value_root.update()

        screen.blit(fondo, (0,0))
        numbers_nodes.draw(screen)
        values.draw(screen)
        value_root.draw(screen)
        text_tittle.draw(screen)
        text1.draw(screen)
        text2.draw(screen)
        text3.draw(screen)
        button_create_binary_tree.draw(screen)
        button_home.draw(screen)
        if visible_tree == True:
            depth = get_depth(binary_treee.root)
            draw_tree(binary_treee.root, (win_width // 2, 300), depth=depth)
        pygame.display.update()
    
def create_binary_tree_one_node(value_root):
    binary_treee.insert(value_root)

def create_binary_tree(value_root, values_nodes):
    binary_treee.insert(value_root)
    if len(values_nodes) > 0:
        for i in range(0, len(values_nodes)):
            binary_treee.insert(values_nodes[i])

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_tree(node, pos, level=1, depth=1):
    if node is not None:
        x, y = pos
        radius = 20
        pygame.draw.circle(screen, BLACK, (x, y), radius)
        font = pygame.font.Font(None, 24)
        text = font.render(str(node.value), True, WHITE)
        screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

        y += win_height // (depth + 1)
        if node.left is not None:
            left_x = x - win_width // (2 ** (level / 1.5))
            pygame.draw.line(screen, BLACK, (x, y - win_height // (depth + 1) + radius), (left_x, y - radius), 2)
            draw_tree(node.left, (left_x, y), level + 1, depth)
        if node.right is not None:
            right_x = x + win_width // (2 ** (level / 1.5))
            pygame.draw.line(screen, BLACK, (x, y - win_height // (depth + 1) + radius), (right_x, y - radius), 2)
            draw_tree(node.right, (right_x, y), level + 1, depth)

def get_depth(node):
    if node is None:
        return 0
    else:
        return max(get_depth(node.left), get_depth(node.right)) + 1
principal()