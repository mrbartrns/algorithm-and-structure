# tree class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def get_specific_value(self, node, n):
        if n == 1:
            return node.data
        else:
            queue = [node]
            k = 1
            while queue:
                to_visit = queue.pop(0)
                if k == n // 2:
                    return to_visit.data
                if to_visit.left:
                    queue.append(to_visit.left)
                if to_visit.right:
                    queue.append(to_visit.right)
                k += 1

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

    def inorder(self, node):
        """
        오름차순으로 탐색
        """
        if node is not None:
            if node.left:
                self.inorder(node.left)
            print(node.data, end=" ")
            if node.right:
                self.inorder(node.right)


def push(arr, tree):
    if len(arr) == 1:
        tree.insert(arr[0])
    elif len(arr) == 0:
        return
    else:
        root_idx = len(arr) // 2
        tree.insert(arr[root_idx])
        push(arr[:root_idx], tree)
        push(arr[root_idx + 1 :], tree)


# n = 1000
# arr = [i for i in range(1, n + 1)]
# tree = BST()
# push(arr, tree)
# print("tree.root:", tree.root.data)
# tree.levelorder(tree.root)
# print()
# tree.inorder(tree.root)
# print()
# print(tree.get_specific_value(tree.root, n))

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [i for i in range(1, n + 1)]
    tree = BST()
    push(arr, tree)
    tree.preorder(tree.root)
    print()
    tree.levelorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    print(f"#{tc + 1} {tree.root.data} {tree.get_specific_value(tree.root, n)}")
