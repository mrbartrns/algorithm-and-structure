# BOJ 9328 열쇠
from collections import deque
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx, mask):
    q = deque()
    ret = mask
    if graph[sy][sx] == "$":
        documents.add((sy, sx))
    elif ord("a") <= ord(graph[sy][sx]) <= ord("z"):
        ret |= 1 << (ord(graph[sy][sx]) - ord("a"))
    visited[sy][sx] = True
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N + 2 or nx < 0 or nx >= M + 2:
                continue
            if visited[ny][nx]:
                continue
            if graph[ny][nx] == "*":
                continue
            # check ny, nx is the lock
            if ord("A") <= ord(graph[ny][nx]) <= ord("Z"):
                if not (ret & (1 << (ord(graph[ny][nx]) - ord("A")))):
                    continue
            # check ny, nx is the key
            if ord("a") <= ord(graph[ny][nx]) <= ord("z"):
                ret |= 1 << (ord(graph[ny][nx]) - ord("a"))
            # check ny, nx is the document
            if graph[ny][nx] == "$":
                documents.add((ny, nx))
            visited[ny][nx] = True
            q.append((ny, nx))
    return ret


def memset(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = value


T = int(si().strip())
for _ in range(T):
    N, M = map(int, si().strip().split(" "))
    graph = [["." for _ in range(M + 2)] for _ in range(N + 2)]
    keys = 0
    visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]
    documents = set()
    for i in range(N):
        arr = list(si().strip())
        for j in range(M):
            graph[i + 1][j + 1] = arr[j]
    kk = list(si().strip())
    for k in kk:
        if k == "0":
            break
        keys |= 1 << ord(k) - ord("a")
    prev = keys
    while True:
        keys = bfs(0, 0, prev)
        if keys == prev:
            break
        prev = keys
        memset(visited, False)
    print(len(documents))
