# BOJ 11286
import heapq
import sys

si = sys.stdin.readline
n = int(si())

# 큐에 넣을 때 ()튜플 형식으로 삽입 후 이후의 값을 꺼내기
q = []
for _ in range(n):
    number = int(si())
    if number != 0:
        heapq.heappush(q, (abs(number), number))
    else:
        if q:
            _, val = heapq.heappop(q)
            print(val)
        else:
            print(0)
