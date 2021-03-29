# BOJ 7662
import heapq
import sys

si = sys.stdin.readline
t = int(si())
for _ in range(t):
    min_q = []
    max_q = []
    visited = [False] * 1000001
    n = int(si())
    for i in range(n):
        op, num = si().split()
        if op == "I":
            heapq.heappush(min_q, (int(num), i))
            heapq.heappush(max_q, (-int(num), i))
            visited[i] = True
        elif int(num) == 1:
            while max_q and not visited[max_q[0][1]]:
                heapq.heappop(max_q)
            if max_q:
                _, idx = heapq.heappop(max_q)
                visited[idx] = False
        else:
            while min_q and not visited[min_q[0][1]]:
                heapq.heappop(min_q)
            if min_q:
                _, idx = heapq.heappop(min_q)
                visited[idx] = False
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    print(f"{-max_q[0][0]} {min_q[0][0]}" if max_q and min_q else "EMPTY")
