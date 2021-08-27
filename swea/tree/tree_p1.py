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
        visited = [False]
        self.root = self._insert_value(self.root, parent, child, visited)
        return self.root is not None

    def _insert_value(self, node, parent, child, visited):

        if not node:
            node = Node(child)
            visited[0] = True

        else:
            if node.idx == parent and (not node.left or not node.right):
                if not node.left:
                    node.left = self._insert_value(node.left, parent, child, visited)
                elif not node.right:
                    node.right = self._insert_value(node.right, parent, child, visited)
            else:
                if not visited[0] and node.left:
                    node.left = self._insert_value(node.left, parent, child, visited)
                if not visited[0] and node.right:
                    node.right = self._insert_value(node.right, parent, child, visited)
        return node

    def preorder(self, node):
        if node is not None:
            print(node.idx, end=" ")
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
            print(to_visit.idx, end=" ")
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
    for y in range(0, len(info), 2):
        parent = info[y]
        child = info[y + 1]
        tree.insert(parent, child)
    print(f"#{tc + 1} {tree.size(sub)}")
"""


def find_value(node, value, counts, visited):
    if node.data == value:
        counts[0] += 1
        counts[1] = True

    elif counts[1] and node.data not in visited:
        counts[0] += 1

    if node is not None:
        if node.data not in visited:
            visited.append(node.data)
        if node.left:
            find_value(node.left, value, counts, visited)
        if node.right:
            find_value(node.right, value, counts, visited)
        if node.data == value:
            counts[1] = False


# data = [2, 1, 2, 5, 1, 6, 5, 3, 6, 4]
# data = [2, 6, 6, 4, 6, 5, 4, 1, 5, 3]
data = [7, 6, 7, 4, 6, 9, 4, 11, 9, 5, 11, 8, 5, 3, 5, 2, 8, 1, 8, 10]
# data = [2, 1, 2, 1, 1, 2, 1, 2]
tree = Tree()
for i in range(0, len(data), 2):
    parent = data[i]
    child = data[i + 1]
    tree.insert(parent, child)
# tree.levelorder(tree.root)
# print()
visited = []
counts = [0, False]
find_value(tree.root, 1, counts, visited)
print(counts[0])

# tree.preorder(tree.root)