class NaryNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class NaryTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def add_root(self, value):
        self.root = NaryNode(value)
        self.length += 1
        return True

    def add_node(self, value, values):
        if self.root is None:
            self.root = NaryNode(value)
            node_parent = self.root
        else:
            node_parent = self.buscar_nodo_sin_hijos(self.root, value)
        if node_parent:
            if len(values) == 0:
                node = NaryNode(None)
                node_parent.children.append(node)
                return True
            else:
                for x in range(0,len(values)):
                    new_node = NaryNode(values[x])
                    node_parent.children.append(new_node)
                    self.length += 1
                return True
        else:
            return False
        
    def eliminar_nodo(self, value):
        aux = self.eliminar_nodo_sin_hijos(self.root, value)
        if aux == True:
            return True
        else:
            return False

    def eliminar_nodo_sin_hijos(self, root, value):
        if root is None:
            return None
        if root.value == value:
            if not root.children:
                return root
        for hijo in root.children:
            current_node = self.buscar_nodo_sin_hijos(hijo, value)
            if current_node is not None:
                current_node.value = None
                return True
        return False

    def buscar_nodo_sin_hijos(self, root, value):
        if root is None:
            return None
        if root.value == value:
            if not root.children:
                return root
        for hijo in root.children:
            resultado = self.buscar_nodo_sin_hijos(hijo, value)
            if resultado is not None:
                return resultado
        return None
    
    def delete_nary_tree(self):
        self.delete_nary_tree_recursive(self.root)
        self.root = None
        self.length = 0

    def delete_nary_tree_recursive(self, node):
        if node is not None:
            for hijo in node.children:
                self.delete_nary_tree_recursive(hijo)
            del node

    def level_order(self):
        result = []
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            if current_node.value is not None:
                result.append(current_node.value)
            queue.extend(current_node.children)

        return result