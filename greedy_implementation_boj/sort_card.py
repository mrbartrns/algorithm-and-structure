# BOJ 1715
import heapq
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

q = []
n = int(si())
for _ in range(n):
    heapq.heappush(q, int(si()))

ret = []
while True:
    temp = []
    for _ in range(2):
        if q:
            c = heapq.heappop(q)
            temp.append(c)
    if len(temp) > 1:
        val = sum(temp)
        ret.append(val)
        heapq.heappush(q, val)
    else:
        break
print(ret)
print(sum(ret))
