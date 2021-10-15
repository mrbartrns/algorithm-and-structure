# BOJ 1939 중량 제한
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def bfs(s, e, m):
    que = deque()
    parents = [i for i in range(N + 1)]
    que.append(s)
    while que:
        node = que.popleft()
        if node == e:
            return True
        for nxt, cost in graph[node]:
            if m > cost:
                continue
            if get_parent(parents, node) != get_parent(parents, nxt):
                union_parent(parents, node, nxt)
                que.append(nxt)
    return False


end = 0
start = int(1e12)

N, M = map(int, si().split(" "))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))
    start = min(start, c)
    end = max(end, c)

start_node, end_node = map(int, si().split(" "))
answer = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(start_node, end_node, mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
