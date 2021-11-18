# BOJ 17472 다리 만들기 2
"""
모든 섬을 연결하는 다리 길이의 최솟값
-> kruskal 알고리즘을 사용할 수 있을듯
1. 모든 섬을 라벨링하고 라벨링 한 숫자들을 기억해둔다.
2. 1부터 N까지 모든 섬에 대하여 같은 라벨끼리 bfs를 한다. bfs를 통하여 모든 방문하지 않은
같은 라벨을 방문한다.
2-1. 만약 다음에 방문할 좌표가 0이라면 그 현재 탐색 방향으로 계속해서 이동해본다.
이동한 좌표의 값이 0도 아니면서 같은 라벨이 아니라면 인접 행렬에 두 라벨과 이동거리를 저장한다.
"""
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find(arr, a):
    if a == arr[a]:
        return a
    arr[a] = find(arr, arr[a])
    return arr[a]


def union(arr, a, b):
    a = find(arr, a)
    b = find(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def kruskal():
    adj.sort(key=lambda x: x[2])
    parents = [i for i in range(label_number + 1)]
    ret = 0
    edge = 0
    for a, b, c in adj:
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            ret += c
            edge += 1
        if edge == label_number - 1:
            return ret
    return -1


def get_bridge_length(sy, sx, d, label_graph_value):
    count = 0
    y, x = sy, sx
    while True:
        if y < 0 or y >= N or x < 0 or x >= M:
            y -= dy[d]
            x -= dx[d]
            break
        if label_graph[y][x] > 0:
            break
        y += dy[d]
        x += dx[d]
        count += 1
    if label_graph_value != label_graph[y][x] and label_graph[y][x] > 0 and count > 1:
        adj.append((label_graph_value, label_graph[y][x], count))


def make_adj(sy, sx, label_graph_value):
    q = deque()
    visited[sy][sx] = True
    q.append((sy, sx))
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if not visited[ny][nx]:
                if label_graph[ny][nx] == label_graph_value:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                elif label_graph[ny][nx] == 0:
                    get_bridge_length(ny, nx, i, label_graph_value)


def bfs(sy, sx):
    q = deque()
    visited[sy][sx] = True
    label_graph[sy][sx] = label_number
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                label_graph[ny][nx] = label_number
                q.append((ny, nx))


N, M = map(int, si().split(" "))
adj = []
graph = [list(map(int, si().split(" "))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
label_graph = [[0 for _ in range(M)] for _ in range(N)]
label_number = 0

# labelling
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] > 0:
            label_number += 1
            bfs(i, j)

visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j] and label_graph[i][j] > 0:
            make_adj(i, j, label_graph[i][j])

print(kruskal())
