# get subtree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, parent, child):
        if not self.root:
            self.root = Node(parent)
        self.root = self._insert_value(self.root, parent, child)
        return self.root is not None

    def _insert_value(self, node, parent, child, visited=False):

        if not node:
            node = Node(child)
            visited = True

        else:
            if node.data == parent and (not node.left or not node.right):
                if not node.left:
                    node.left = self._insert_value(node.left, parent, child, visited)
                elif not node.right:
                    node.right = self._insert_value(node.right, parent, child, visited)
            else:
                if not visited and node.left:
                    node.left = self._insert_value(node.left, parent, child)
                if not visited and node.right:
                    node.right = self._insert_value(node.right, parent, child)
        return node

    def size(self, key):
        node = self.find(key)
        return node.size() if node else 0

    def find(self, key):
        """
        data를 찾는 함수
        help function
        input: key
        return: boolean if node.data == key or node is None
        """
        return self._find_value(self.root, key)

    def _find_value(self, node, key):
        """
        data를 찾기 위한 재귀함수
        사용시에는 find 함수만 사용할 것
        input: node, key (init: self.root)
        return: recursive function
        """
        if not node:
            return None
        elif node.data == key:
            return node

        else:
            if key < node.data:
                node = self._find_value(node.left, key)
            else:
                node = self._find_value(node.right, key)
            return node

    def preorder(self, node):
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


"""
t = int(input())
for tc in range(t):
    tree = Tree()
    e, sub = map(int, input().split())
    info = [int(x) for x in input().split()]
    for i in range(0, len(info), 2):
        parent = info[i]
        child = info[i + 1]
        tree.insert(parent, child)
    print(f"#{tc + 1} {tree.size(sub)}")
"""

# data = [2, 1, 2, 5, 1, 6, 5, 3, 6, 4]
# data = [2, 6, 6, 4, 6, 5, 4, 1, 5, 3]
# data = [7, 6, 7, 4, 6, 9, 4, 11, 9, 5, 11, 8, 5, 3, 5, 2, 8, 1, 8, 10]
data = [1, 1, 1, 1, 1, 1, 1, 1]
tree = Tree()
for i in range(0, len(data), 2):
    parent = data[i]
    child = data[i + 1]
    tree.insert(parent, child)
    tree.levelorder(tree.root)
    print()
# print(tree.size(5))


# tree.preorder(tree.root)