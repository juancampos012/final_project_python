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
        elif self.contains(value) is False:
            self.insert_recursive(self.root, value)
        else:
            return True
    
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
    
    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._contains_recursive(current.left, value)
        else:
            return self._contains_recursive(current.right, value)

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
    
    def traverse_level_order(self):
        result = []
        if self.root is None:
            return result

        queue = [self.root]
        current_index = 0

        while current_index < len(queue):
            current_node = queue[current_index]
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            current_index += 1

        return result
    
    def traverse_inorder(self):
        if self.root is None:
            return
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def traverse_postorder(self):
        if self.root is None:
            return
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def traverse_preorder(self):
        if self.root is None:
            return
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def delete_node(self, root, value):
        if root is None:
            return root
        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                temp = self.find_max(root.left)
                root.value = temp.value
                root.left = self.delete_node(root.left, temp.value)
        return root

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node