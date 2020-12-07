# linear queue
# 재귀함수도 중요함! 다시 복습하기 책으로


class LQueue:
    def __init__(self, n):
        self.queue = [0] * (n + 1)
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.isFull():
            print("queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            self.front += 1
            return self.queue[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == len(self.queue) - 1

    def QPeek(self):
        return self.queue[self.front + 1]


# circle queue
class CQueue:
    def __init__(self, n):
        self.queue = [0] * (n + 1)
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
        return self.front == self.rear