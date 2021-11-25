"""
현재 좌표를 방문
연결된 다음 좌표를 방문
연결된 다음 좌표는 다음 세가지 경우가 존재
1. 아직 방문하지 않은 좌표일 경우
2. 이미 방문한 좌표일 경우
3. 범위를 벗어난 지점일 경우
1의 경우 -> 그대로 방문하면 됨
2의 경우 이 지점에서 세이프존이 추가됨 -> 추가된 뒤에 어떻게 처리해야 하는지가 중요
3의 경우 세이프좀이 추가됨
"""
# BOJ 16724 피리 부는 사나이
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(10000000)
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
OPER = {"U": 0, "D": 1, "L": 2, "R": 3}

N, M = map(int, si().split(" "))
adj = [list(si().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
finished = [[False for _ in range(M)] for _ in range(N)]
count = [0]


def dfs(y, x):
    visited[y][x] = True
    o = adj[y][x]
    d = OPER[o]
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        count[0] += 1
        return
    elif not visited[ny][nx]:
        dfs(ny, nx)
    elif visited[ny][nx] and not finished[ny][nx]:
        count[0] += 1
    finished[y][x] = True


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
print(count[0])
