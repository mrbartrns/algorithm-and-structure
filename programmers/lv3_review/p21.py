# [카카오] 길 찾기 게임
import heapq
import sys

sys.setrecursionlimit(10001)


class Node:
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, idx):
        self.root = self._insert(self.root, data, idx)
        return self.root is not None

    def _insert(self, node, data, idx):
        if not node:
            return Node(data, idx)

        if data < node.idx:
            node.left = self._insert(node.left, data, idx)
        else:
            node.right = self._insert(node.right, data, idx)
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


def solution(node_info):
    q = []
    ret = []
    tree = Tree()
    for i in range(len(node_info)):
        heapq.heappush(q, (-node_info[i][1], node_info[i][0], i + 1))
    while q:
        level, data, idx = heapq.heappop(q)
        tree.insert(data, idx)
    ret.append(tree.preorder(tree.root))
    ret.append(tree.postorder(tree.root))
    return ret


if __name__ == "__main__":
    node_info = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
    print(solution(node_info))
