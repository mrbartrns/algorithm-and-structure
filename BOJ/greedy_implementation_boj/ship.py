# BOJ 1092 배
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n = int(si())
container = list(map(int, si().split()))
container.sort()
m = int(si())
boxes = list(map(int, si().split()))
boxes.sort(reverse=True)


class Node:
    def __init__(self, data, idx) -> None:
        self.prev = None
        self.next = None
        self.data = data
        self.idx = idx


def solve(container, boxes):
    if boxes[0] > container[-1]:
        return -1

    answer = 0
    visited = [False] * m
    linked_list = [Node(boxes[0], 0)]
    cnt = 0
    for i in range(m):
        node = Node(boxes[i], i)
        prev = linked_list[i - 1]
        prev.next = node
        node.prev = prev
        linked_list.append(node)

    while True:
        if cnt >= m:
            return answer
        for i in range(n):
            s = 0
            j = 0
            while j < m and (visited[j] or linked_list[j].data > container[i]):
                j += 1

            cur_node = linked_list[j]
            while cur_node:
                if s + cur_node.data <= container[i] and not visited[cur_node.idx]:
                    s += cur_node.data
                    visited[cur_node.idx] = True
                    cnt += 1
                    prev = cur_node.prev
                    nxt = cur_node.next
                    if prev:
                        prev.next = nxt
                    if nxt:
                        nxt.prev = prev
                cur_node = cur_node.next
        answer += 1


print(solve(container, boxes))
