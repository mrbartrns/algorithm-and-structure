# [카카오] 길 찾기 게임
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, idx, data) -> None:
        self.idx = idx
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, idx, data):
        self.root = self._insert(self.root, idx, data)
        return self.root is not None

    def _insert(self, node, idx, data):
        if not node:
            return Node(idx, data)
        if data < node.data:
            node.left = self._insert(node.left, idx, data)
        else:
            node.right = self._insert(node.right, idx, data)
        return node

    def preorder(self, node):
        ret = [node.idx]
        if node.left:
            ret += self.preorder(node.left)
        if node.right:
            ret += self.preorder(node.right)
        return ret

    def postorder(self, node):
        ret = []
        if node.left:
            ret += self.postorder(node.left)
        if node.right:
            ret += self.postorder(node.right)
        ret += [node.idx]
        return ret


def solution(nodeinfo):
    tree = Tree()
    answer = []
    table = []
    for i in range(len(nodeinfo)):
        table.append((nodeinfo[i][0], nodeinfo[i][1], i + 1))
    table.sort(key=lambda x: -x[1])
    for i in range(len(table)):
        tree.insert(table[i][2], table[i][0])
    answer.append(tree.preorder(tree.root))
    answer.append(tree.postorder(tree.root))
    return answer


if __name__ == "__main__":
    nodeinfo = [
        [5, 3],
        [11, 5],
        [13, 3],
        [3, 5],
        [6, 1],
        [1, 3],
        [8, 6],
        [7, 2],
        [2, 2],
    ]
    print(solution(nodeinfo))
