class Queue:
    def __init__(self, n):
        self.queue = [0] * n
        self.front = -1
        self.rear = -1

    def enQueue(self, item):
        if self.isFull():
            print("queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front += 1
            return self.queue[self.front]

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return self.rear == len(self.queue) - 1


### 선형 큐의 문제점은 front와 rear가 초기화되지 않으면 메모리 소모가 크다는 문제점이 존재함