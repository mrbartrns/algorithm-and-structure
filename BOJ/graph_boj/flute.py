# BOJ 16724 피리부는 사나이
"""
지도 어느 구역에서도 세이프존에 들어갈 수 있게 만드는 세이프존의 최소 개수 구하기
세이프존을 설치해야 할 기준 
- 지도 어디에 위치해있더라도 세이프존에 들어가야함
-- 확인하는 법: 
1) 2차원 그래프에서 union-find 실행 방법? -> 3차원 visited 배열로 관리하기
2) 현재 좌표와 다음에 이동할 좌표를 비교
2-1) 현재 좌표와 다음에 이동할 좌표가 서로 이어져있지 않다면, union후 다음 좌표로 이동하기
3) 다음에 이동할 좌표가 그래프의 범위를 벗어났다면, 개수 1을 추가한다.

-> 현재 방법: 일단 방법은 맞는것 같은데 시간초과가 발생
"""
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(10000000)
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
OPER = {"U": 0, "D": 1, "L": 2, "R": 3}

N, M = map(int, si().split(" "))
adj = [list(si().strip()) for _ in range(N)]
parents = [[(i, j) for j in range(M)] for i in range(N)]
counts = [[0 for _ in range(M)] for _ in range(N)]


def find(arr, y, x):
    if arr[y][x] == (y, x):
        return (y, x)
    arr[y][x] = find(arr, arr[y][x][0], arr[y][x][1])
    return arr[y][x]


def union(arr, y1, x1, y2, x2):
    y1, x1 = find(arr, y1, x1)
    y2, x2 = find(arr, y2, x2)
    if y1 < y2:
        arr[y2][x2] = (y1, x1)
    else:
        if y1 == y2:
            if x1 < x2:
                arr[y2][x2] = (y1, x1)
            else:
                arr[y1][x1] = (y2, x2)
        else:
            arr[y1][x1] = (y2, x2)


def dfs(y, x):
    # 현재좌표와 다음좌표의 get_parent가 같다면 이미 방문한 좌표이다.
    o = adj[y][x]
    d = OPER[o]
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        py, px = find(parents, y, x)
        counts[py][px] = 1
    else:
        if find(parents, y, x) != find(parents, ny, nx):
            union(parents, y, x, ny, nx)
            dfs(ny, nx)
        else:
            py, px = find(parents, y, x)
            counts[py][px] = 1


ret = 0
for i in range(N):
    for j in range(M):
        if find(parents, i, j) == (i, j):
            dfs(i, j)
for i in range(N):
    for j in range(M):
        ret += counts[i][j]
print(ret)
