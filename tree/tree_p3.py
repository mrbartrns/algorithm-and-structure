"""
MinHeap 구현하기
"""


class MinHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, key):
        self.data.append(key)
        idx = len(self.data) - 1
        while idx > 1:
            if self.data[idx] < self.data[idx // 2]:
                self.data[idx], self.data[idx // 2] = (
                    self.data[idx // 2],
                    self.data[idx],
                )
                idx //= 2
            else:
                break

    def __str__(self):
        return str(self.data[1:])

    def parent_node_sum(self):
        _sum = self._parent_node_sum(len(self.data) - 1)
        return _sum

    def _parent_node_sum(self, idx):
        if idx > 1:
            return self.data[idx // 2] + self._parent_node_sum(idx // 2)
        else:
            return 0


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    heap = MinHeap()
    for i in arr:
        heap.insert(i)
    print(f"#{tc + 1} {heap.parent_node_sum()}")

# arr = [3, 1, 4, 16, 23, 12]
# arr = [7, 2, 5, 3, 4, 6]
# arr = [18, 57, 11, 52, 14, 45, 63, 40]
# heap = MinHeap()
# for i in arr:
#     heap.insert(i)
# print(heap)
# print(heap.parent_node_sum())