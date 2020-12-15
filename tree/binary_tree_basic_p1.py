class Node:
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


class BST:
    """
    BST(Binary Seach Tree)는 Node 클래스를 입력받는다.
    """

    def __init__(self):
        self.root = None

    # size와 depth는 node의 함수를 그대로 사용한다.
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
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            elif data > node.data:
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

    # 이 함수는 트리에서 노드를 삭제하는데 사용된다.
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, key):
        self.root = self._delete_value(self.root, key)
        print("return값:", self.root.data)

    def _delete_value(self, node, key):
        if node is None:
            return node

        if key < node.data:
            print("실행 전 node.left:", node.left.data)
            node.left = self._delete_value(node.left, key)
            print("실행 후 node.left:", node.left.data)
            return node  # node를 return 하는 이유?

        elif key > node.data:
            node.right = self._delete_value(node.right, key)
            return node

        else:  # key == node.data
            print("값을 찾았음")
            if not node.left and not node.right:
                return None  # parent node에 None을 할당
            elif not node.left:
                return node.right  # parent node에 node.right를 할당 (parent node는 node)
            elif not node.right:
                return node.left  # parent node에 node.left를 할당 (parent node는 node)
            else:
                print("두개의 노드")
                # child node가 두개일때, 우측 node에서 최솟값을 가져온 후, 최솟값을 삭제한다.
                min_node = self.min_value_node(node.right)
                node.data = min_node.data
                node.right = self._delete_value(node.right, min_node.data)
                return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(7)
    bst.insert(5)
    bst.insert(8)
    bst.insert(3)
    bst.insert(6)
    bst.insert(1)
    bst.insert(4)

    print(bst._delete_value(bst.root, 3))
    bst.inorder(bst.root)