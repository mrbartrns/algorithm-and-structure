# BOJ 1092 배
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n = int(si())
container = list(map(int, si().split()))
container.sort(reverse=True)
m = int(si())
boxes = list(map(int, si().split()))
boxes.sort(reverse=True)


def solve(container, boxes):
    if boxes[0] > container[0]:
        return -1

    answer = 1
    while True:
        for i in range(n):
            for j in range(len(boxes)):
                if container[i] >= boxes[j]:
                    boxes.pop(j)
                    break
            if not boxes:
                return answer
        answer += 1


print(solve(container, boxes))
