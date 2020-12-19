# linear queue
class LQueue:
    def __init__(self, n):
        self.queue = [0] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.is_full():
            print("queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            self.front += 1
            return self.queue[self.front]

    def peek(self):
        return self.queue[self.front + 1]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == len(self.queue) - 1

    def __str__(self):
        return str(self.queue)


# circle queue
class CQueue:
    def __init__(self, n):
        self.queue = [0] * (n + 1)
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.is_full():
            print("queue is full")
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

    def peek(self):
        return self.queue[(self.front + 1) % len(self.queue)]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % len(self.queue) == self.front

    def __str__(self):
        return str(self.queue)
