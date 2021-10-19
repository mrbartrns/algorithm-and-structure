# BOJ 2234 성벽
from collections import deque
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def get_label_counts(label_arr, label_number):
    ret = [0] * label_number
    for i in range(M):
        for j in range(N):
            ret[label_arr[i][j]] += 1
    return ret


def get_maximum_value(label_count_arr):
    ret = 0
    for y in range(M):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= M or nx < 0 or nx >= N:
                    continue
                temp = label_count_arr[visited[y][x]]
                s = 0
                if visited[ny][nx] != visited[y][x]:
                    s = max(s, label_count_arr[visited[ny][nx]])
                ret = max(ret, temp + s)
    return ret


def bfs(sy, sx, label_number):
    """벽을 뚫지 않았을때 라벨을 처리하는 함수"""
    que = deque()
    visited[sy][sx] = label_number
    que.append((sy, sx))
    while que:
        y, x = que.popleft()

        # 칸을 통과할 수 없는 경우
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if graph[y][x] & (1 << i):
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = label_number
                que.append((ny, nx))


N, M = map(int, si().split(" "))
graph = [list(map(int, si().split(" "))) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
label = 1
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, label)
            label += 1
label_cnt_arr = get_label_counts(visited, label)
answer = get_maximum_value(label_cnt_arr)
print(label - 1)
print(max(label_cnt_arr))
print(answer)
