class NaryNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class NaryTree:
    def __init__(self):
        self.root = None

    def add_root(self, value):
        self.root = NaryNode(value)
        print("Added root")

    def add_node(self, value, parent):
        new_node = NaryNode(value)
        node_parent = self._buscar_nodo(self.root, parent)

        if node_parent:
            node_parent.children.append(new_node)
            print("Added node")
        else:
            print(f"No se encontró el nodo con valor {parent}.")

    def _buscar_nodo(self, node, value):
        if node.value == value:
            return node

        for hijo in node.children:
            node_search = self._buscar_nodo(hijo, value)
            if node_search:
                return node_search

        return None

    def preorder(self, node=None):
        if node is None:
            node = self.root

        result = [node.value]
        for child in node.children:
            result.extend(self.preorder(child))

        return result

    def postorder(self, node=None):
        if node is None:
            node = self.root

        result = []
        for child in node.children:
            result.extend(self.postorder(child))
        result.append(node.value)

        return result

    def inorder(self, node=None):
        if node is None:
            node = self.root

        values = []
        for child in node.children:
            values.extend(self.inorder(child))
        values.append(node.value)
        return values

    def level_order(self):
        result = []
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)
            queue.extend(current_node.children)

        return result