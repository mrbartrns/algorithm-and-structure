def get_seq_num1(arr, m):
    return arr[m % len(arr)]


# arr1 = [5527, 731, 31274]
# arr2 = [18140, 14618, 18641, 22536, 23097]
# arr3 = [17236, 31594, 29094, 2412, 4316, 5044, 28515, 24737, 11578, 7907]
# print(get_seq_num1(arr1, 10))
# print(get_seq_num1(arr2, 12))
# print(get_seq_num1(arr3, 23))


class CQueue:
    def __init__(self, size):
        self.queue = [0] * (size + 1)
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.isFull():
            print("queue is full")
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

    def isFull(self):
        return (self.rear + 1) % len(self.queue) == self.front

    def isEmpty(self):
        return self.rear == self.front

    def Qpeek(self):
        return self.queue[self.front + 1]

    def __repr__(self):
        return str(self.queue)


def get_seq_num2(arr, m):
    for _ in range(m):
        el = arr.dequeue()
        arr.enqueue(el)
    return arr.Qpeek()


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    queue = CQueue(len(arr))
    for i in arr:
        queue.enqueue(i)
    print(f"#{i + 1} {get_seq_num2(queue, m)}")
