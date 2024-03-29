"""
tree 자료구조 만들기(이진탐색 트리 구현)
"""


class Node:
    """
    1. node는 데이터와 childNode의 참조값 두개를 저장한다.
    2. size와 depth는 재귀적으로 구현한다. 재귀는, 귀납적으로 생각하여 메소드의 값이 해결되었다고 가정하고 코드를 작성해나간다. (종결조건만 잘 잡아주면 된다)
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return left_depth + 1 if left_depth > right_depth else right_depth + 1

    def __repr__(self):
        return str(self.data)


class BinaryTree:
    """
    class BinaryTree는 node클래스를 기본으로 받는다고 가정하고 코드를 작성한다.
    """

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
        if node is None:
            node = Node(data)
        else:
            if data <= node.idx:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node  # return값은 신경 쓸 필요 없다

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    # get minimum value in the tree
    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, key):
        # self.root의 값이 바뀐다면, 값을 할당한다.
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node, key):
        if not node:
            return None

        # key가 처음에 self.root의 값과 같지 않다면, key < node.data 또는 key > node.data 중 하나일 것이다.
        # key가 node의 data보다 작을 경우, 왼쪽의 값을 탐색 후 제거
        if key < node.idx:
            node.left = self._delete_node(node.left, key)
            return node

        # key가 node의 data보다 클 경우, 오른쪽의 값을 탐색 후 제거
        elif key > node.idx:
            node.right = self._delete_node(node.right, key)
            return node

        else:  # node.data == data
            if not node.left and not node.right:
                return None

            elif node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            else:
                min_node = self.min_value_node(node.right)
                node.idx = min_node.idx
                node.right = self._delete_node(node.right, min_node.idx)
                return node

    # tree를 출력하는 것 역시 재귀함수로 나타낸다.
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.idx, end=" ")
            self.inorder(node.right)


if __name__ == "__main__":
    boo = BinaryTree()

    boo.insert(5)
    boo.insert(1)
    boo.insert(9)
    boo.insert(3)
    boo.insert(7)
    boo.insert(2)
    boo.insert(8)

    # boo.inorder(boo.root)
    print(boo.root)
    print(boo.delete(1))
    print(boo.root)
