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

    def add_node(self, nivel, pocision, value):
        node_parent = self.search_by_level_and_position(self.root, nivel, pocision)
        if node_parent:
            new_node = NaryNode(value)
            node_parent.children.append(new_node)
            return True
        else:
            return False

    def search_by_level_and_position(self, root, level, position):
        if level == 1 and position == 1:
            return root
        if root is None:
            return None
        queue = []
        queue.append(root)
        current_level = 1
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if current_level == level and i+1 == position:
                    return node
                for child in node.children:
                    queue.append(child)
            current_level += 1
        return None

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
    
    def delete_nary_tree(self):
        self.delete_nary_tree_recursive(self.root)
        self.root = None

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
            result.append(current_node.value)
            queue.extend(current_node.children)

        return result