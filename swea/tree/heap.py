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
        print("appended:", self.data)
        i = len(self.data) - 1  # 맨 앞의 원소는 None이다.
        while i > 1:
            if self.data[i] > self.data[i // 2]:
                self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                print("swaped:", self.data)
                i //= 2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            print("removed:", self.data)
            self.data.pop()
            self.max_heapify(1)
        else:
            data = None
        return data

    def max_heapify(self, idx: int):
        left = 2 * idx
        right = (2 * idx) + 1
        largest = idx
        print("idx:", idx, "left:", left, "right:", right)
        if left < len(self.data) and self.data[left] > self.data[largest]:
            print("self.data[left] > self.data[idx]")
            largest = left
            print("largest:", largest)

        if right < len(self.data) and self.data[right] > self.data[largest]:
            print("self.data[idx] > self.data[right]")
            largest = right
            print("largest:", largest)

        if largest != idx:
            print("largest != idx")
            self.data[idx], self.data[largest] = self.data[largest], self.data[idx]
            print(self.data)
            self.max_heapify(largest)

    def __str__(self):
        return str(self.data[1:])


if __name__ == "__main__":
    heap = MaxHeap()
    for i in range(1, 14):
        heap.insert(i)
        print(heap)
    heap.remove()
    print(heap)