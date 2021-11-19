# BOJ 16946 벽 부수고 이동하기 4
"""
벽을 부수고 이동할 수 있는 곳으로 변경한다
그 위치에서 이동할 수 있는 칸의 개수를 센다
맵의 형태로 정답을 출력한다. 원래 빈칸인 곳은 0을 출력하고 벽인곳은 이동할 수 있는 
칸의 개수를 센다
그래프를 탐색하는 것은 1000 * 1000 = 1000000 이기 때문에 충분해 보이지만,
모든 1인 위치에 대하여 탐색해야하므로 1000 * 1000 * 1000이므로 시간초과가 발생할
여지가 있다.

1. 0인 지점에 대하여 dfs 또는 bfs를 하여 0의 개수를 센다.
2. 다시 bfs 또는 dfs를 하여 주변에 1이 있다면, 현재 0의 개수를 1인 지점에 더한다.
zero counts 배열 필요
** 이럴경우 문제에서 요구하는 조건과 출력을 동일하게 맞출 수 있다.

### MOD로 나누어야 하는 경우, 나누는 것을 잊지 않도록 미리 작성해 두기
"""
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
MOD = 10


def count_zero(sy, sx):
    q = deque()
    count = 0
    visited[sy][sx] = True
    count += 1
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] == 1:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                count += 1
                q.append((ny, nx))
    return count


def save_count(sy, sx, count, label_number):
    q = deque()
    q.append((sy, sx))
    label[sy][sx] = label_number
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] == 1 and label[ny][nx] != label_number:
                label[ny][nx] = label_number
                zero_counts[ny][nx] += count
                zero_counts[ny][nx] %= MOD
                continue
            if graph[ny][nx] == 0 and label[ny][nx] != label_number:
                label[ny][nx] = label_number
                q.append((ny, nx))


N, M = map(int, si().split(" "))
graph = [list(map(int, list(si().strip()))) for _ in range(N)]
label_number = 0
zero_counts = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
label = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            label_number += 1
            zero = count_zero(i, j)
            save_count(i, j, zero, label_number)
        elif graph[i][j] == 1:
            zero_counts[i][j] += 1
            zero_counts[i][j] %= MOD
for i in range(N):
    for j in range(M):
        print(zero_counts[i][j], end="")
    print()
