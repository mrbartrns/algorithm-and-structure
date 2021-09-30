from collections import deque
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def bfs(start):
    que = deque()
    visited[start] = True
    que.append(start)
    cnt = 0
    while que:
        cur_node = que.popleft()
        for nxt in graph[cur_node]:
            if not visited[nxt]:
                visited[nxt] = True
                que.append(nxt)
                cnt += 1
    return cnt


graph = [[] for _ in range(26)]
indegree = [0] * 26
visited = [False] * 26
N, M = map(int, si().split(" "))
for _ in range(M):
    a, b = si().strip().split(" ")
    graph[ord(a) - ord("A")].append(ord(b) - ord("A"))
    indegree[ord(b) - ord("A")] += 1

deactivated = list(si().strip().split(" "))
for i in range(1, len(deactivated)):
    visited[ord(deactivated[i]) - ord("A")] = True


answer = 0
for i in range(26):
    if indegree[i] == 0 and not visited[i]:
        answer += bfs(i)
print(answer)