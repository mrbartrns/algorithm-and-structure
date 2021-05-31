# heap


class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1
        while idx > 1:
            if self.heap[idx] > self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = (
                    self.heap[idx // 2],
                    self.heap[idx],
                )
                idx //= 2
            else:
                break

    def remove(self):
        if len(self.heap) > 1:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
            self.heap.pop()
            self.heapify(1)
        else:
            return -1

    def heapify(self, idx):
        left = 2 * idx
        right = 2 * idx + 1
        largest = idx
        if left < len(self.heap) and self.heap[largest] < self.heap[left]:
            largest = left
        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right
        if idx != largest:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self.heapify(largest)

    def __str__(self):
        return str(self.heap[1:])