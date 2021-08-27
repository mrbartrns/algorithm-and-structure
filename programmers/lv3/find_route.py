# 길찾기 게임
import heapq


class Node:
    def __init__(self, data, idx):
        self._data = data
        self._idx = idx
        self.left = None
        self.right = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def idx(self):
        return self._idx

    @idx.setter
    def idx(self, idx):
        self._idx = idx


class Tree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, data, idx):
        self._root = self._insert_data(self._root, data, idx)
        return self._root is not None

    def _insert_data(self, node, data, idx):
        if not node:
            return Node(data, idx)

        if data < node.idx:
            node.left = self._insert_data(node.left, data, idx)
        else:
            node.right = self._insert_data(node.right, data, idx)
        return node

    def preorder(self, node, arr):
        arr.append(node.idx)
        if node.left:
            self.preorder(node.left, arr)
        if node.right:
            self.preorder(node.right, arr)

    def postorder(self, node, arr):
        if node.left:
            self.postorder(node.left, arr)
        if node.right:
            self.postorder(node.right, arr)
        arr.append(node.idx)

    def get_preorder_data(self):
        ret = []
        self.preorder(self.root, ret)
        return ret

    def get_postorder_data(self):
        ret = []
        self.postorder(self.root, ret)
        return ret


def solution(node_info):
    answer = []
    tree = Tree()
    q = []
    for i in range(len(node_info)):
        current_node = node_info[i]
        heapq.heappush(q, (-current_node[1], current_node[0], i + 1))
    while q:
        current_node = heapq.heappop(q)
        tree.insert(current_node[1], current_node[2])
    answer.append(tree.get_preorder_data())
    answer.append(tree.get_postorder_data())
    return answer


if __name__ == "__main__":
    node_info = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
    print(solution(node_info))
