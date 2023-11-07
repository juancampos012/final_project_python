class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)
    
    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)
    
    def delete_tree(self):
        self.delete_tree_recursive(self.root)
        self.root = None

    def delete_tree_recursive(self, node):
        if node is None:
            return
        self.delete_tree_recursive(node.left)
        
        self.delete_tree_recursive(node.right)
        node.left = None
        node.right = None