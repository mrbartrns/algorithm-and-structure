# BOJ 1707
import sys
from collections import deque

si = sys.stdin.readline


def dfs(v, c):
    visited[v] = c
    for i in graph[v]:
        if visited[i] == 0:  # 여기서 미리 검사
            if not dfs(
                i, 3 - c
            ):  # 상위 스택에서 하나라도 False라면 False를 반환. > 컬러를 계속해서 바꾸는 방법은 상위 숫자에서 그 숫자를 빼는 것이다.
                return False
        elif (
            visited[v] == visited[i]
        ):  # 여기서 검사하는 이유는 현재 노드와 인접한 노드에 대해서 색이 모두 달라야 하기 때문이다.
            return False
    return True  # 맨 마지막에 모두 충족후 참이 되게하려면 마지막에 True를 써야 한다.


def bfs(v, c):
    que = deque([v])
    visited[v] = c
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 3 - visited[v]
            elif visited[v] == visited[i]:
                return False
    return True


t = int(si())
for _ in range(t):
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    answer = True
    for _ in range(m):
        x, y = map(int, si().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 0 and not bfs(i, 1):
            answer = False
            break

    print("YES" if answer else "NO")
