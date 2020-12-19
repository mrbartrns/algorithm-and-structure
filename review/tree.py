# tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return left_size + right_size + 1

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return left_depth + 1 if left_depth > right_depth else right_depth + 1

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self.root.size() if self.root else 0

    def depth(self):
        return self.root.size() if self.root else 0

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.left.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, node, key):
        if node is None:
            return False
        elif node.data == key:
            return True
        else:
            if key < node.data:
                return self._find_value(node.left, key)
            else:
                return self._find_value(node.right, key)

    def get_min_value(self, node):
        if node.left is None:
            return node.data
        else:
            return self._find_value(self, node.left)

    def delete(self, key):
        self.root = self._delete_value(self.root, key)
        return self.root is not None

    def _delete_value(self, node, key):
        if not node:
            return None

        elif key < node.data:
            node.left = self._delete_value(node.left, key)
            return node
        elif key > node.data:
            node.right = self._delete_value(node.right, key)
            return node
        else:
            if not node.left and node.right:
                node = None
            elif node.left and not node.right:
                node = node.left
            elif node.right and not node.left:
                node = node.right
            else:
                min_value = self.get_min_value(node.right)
                node.data = min_value.data
                node.right = self._delete_value(node.right, min_value.data)
            return node

    def preorder(self, node):
        if node:
            print(node.data)
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    def inorder(self, node):
        if node:
            if node.left:
                self.inorder(node.left)
            print(node.data)
            if node.right:
                self.inorder(node.right)

    def postorder(self, node):
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

    def levelorder(self, node):
        queue = [node]
        while queue:
            to_visit = queue.pop(0)
            print(to_visit)
            if to_visit.left:
                queue.append(to_visit.left)
            if to_visit.right:
                queue.append(to_visit.right)
