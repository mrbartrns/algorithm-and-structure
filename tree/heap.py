"""
Heap
- 힙은 최댓값과 최솟값을 빠르게 찾기 위한 자료구조
- 완전 이진트리 형태이므로 배열 사용이 가능
- 힙은 탐색을 하기에는 적절하지 않다. 그러나 삽입/삭제의 연산은 빠르다
"""


class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1  # 맨 앞의 원소는 None이다.
        while i > 1:
            if self.data[i] > self.data[i // 2]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                i //= 2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop()
            self.max_heapify(1)
        else:
            data = None
        return data

    def max_heapify(self, idx: int):
        left = 2 * idx
        right = (2 * idx) + 1
        smallest = idx
        if left < len(self.data) and self.data[idx] < self.data[left]:
            smallest = left

        if right < len(self.data) and self.data[idx] > self.data[right]:
            smallest = right

        if smallest != idx:
            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            self.max_heapify(smallest)