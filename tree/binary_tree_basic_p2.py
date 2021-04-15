# BST


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


class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self.root.size() if self.root else 0

    def depth(self):
        return self.root.depth() if self.root else 0

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if not node:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, node, key):
        if node is None or node.data == key:
            return node is not None
        else:
            if key < node.data:
                return self._find_value(node.left, key)
            else:
                return self._find_value(node.right, key)

    def get_min_value(self, node):
        current = node
        while current:
            current = current.left
        return current

    def delete(self, key):
        self.root = self._delete_value(self.root, key)
        return self.root is not None

    def _delete_value(self, node, key):
        if not node:
            return None
        elif key < node.data:
            node.left = self._delete_value(node.left, key)
        elif key > node.data:
            node.right = self._delete_value(node.right, key)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_value = self.get_min_value(node.right)  # node는 현재 지워야 할 대상
                node.data = min_value.data
                min_value = self._delete_value(min_value, key)
                return node

    #### 트리 순회 메서드 ###
    def preorder(self, node):
        """
        전위순회의 순회 방법
        1. 현재 노드 n을 먼저 방문
        2. 현재 노드의 왼쪽 서브트리를 순회
        3. 현재 노드의 오른쪽 서브트리를 순회
        """
        if node is not None:
            print(node.data, end=" ")
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    def inorder(self, node):
        """
        중위순회의 순회 방법
        1. 현재 노드의 왼쪽 서브트리를 순회
        2. 현재 노드를 방문
        3. 현재 노드의 오른쪽 서브트리를 순회
        """
        if node is not None:
            if node.left:
                self.inorder(node.left)
            print(node.data, end=" ")
            if node.right:
                self.inorder(node.right)

    def postorder(self, node):
        """
        후위순회의 순회 방법
        1. 현재 노드의 왼쪽 서브트리를 순회
        2. 현재 노드의 오른쪽 서브트리를 순회
        3. 현재노드를 방문
        """
        if node is not None:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.data, end=" ")

    def levelorder(self, node):
        """
        레벨순회의 순회 방법
        - 루트가 있는 곳에서 각 레벨마다 좌에서 우로 노드들을 방문(BFS 방식으로 구현)
        """
        queue = [node]
        while queue:
            to_visit = queue.pop(0)
            print(to_visit.data, end=" ")
            if to_visit.left:
                queue.append(to_visit.left)
            if to_visit.right:
                queue.append(to_visit.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(40)
    # bst.insert(4)
    # bst.insert(45)
    # bst.insert(34)
    # bst.insert(55)
    # bst.insert(14)
    # bst.insert(48)
    # bst.insert(13)
    # bst.insert(15)
    # bst.insert(47)
    # bst.insert(49)
    # data = [11, 5, 10, 4, 9, 3, 8, 1, 2, 6, 7]
    # for y in data:
    #     bst.insert(y)
    bst.preorder(bst.root)
    print()
    bst.inorder(bst.root)
    print()
    bst.postorder(bst.root)
    print()