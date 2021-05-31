class CQueue:
    def __init__(self, size: int):
        self.queue = [0] * (size + 1)
        self.front = 0
        self.rear = 0

    def enqueue(self, item: int or float):
        if self.isFull():
            print("Queue is full")
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % len(self.queue) == self.front

    def Qpeek(self):
        # queue의 맨 첫번째 아이템을 반환
        return self.queue[(self.front + 1) % len(self.queue)]

    def __repr__(self):
        return str(self.queue)


# queue의 size가 5라면, 공백을 확인하기 위하여 front에서의 값은 비워둔다. 즉 queue의 사이즈가 5라면 4까지 들어갈 수 있다.

if __name__ == "__main__":
    size = 5
    queue = CQueue(size)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("full")

    print(queue.dequeue())
    queue.enqueue(5)
    print(queue.dequeue())
    queue.enqueue(6)
    print(queue)
