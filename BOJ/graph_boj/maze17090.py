# BOJ 17090 미로 탈출하기
"""
1. 모든 칸에서 시작할 수 있다.
2. 하나의 칸에는 하나의 명령어가 존재하고 그 명령어대로만 이동이 가능하다.
3. 어떠한 칸에 도착하면, 그 칸에서의 경우의 수가 정해진다.
4. 이미 도착했음에도 불구하고 그 경우의 수가 1이 아니라면, 0이다.
dfs를 이용하여 문제를 해결해 볼 수 있겠다.
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
sys.setrecursionlimit(1000000)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
OPER = {"U": 0, "D": 1, "L": 2, "R": 3}

N, M = map(int, si().split(" "))
adj = [list(si().strip()) for _ in range(N)]
cache = [[-1 for _ in range(M)] for _ in range(N)]


def dfs(y, x):
    if y < 0 or y >= N or x < 0 or x >= M:
        return 1
    if cache[y][x] > -1:
        return cache[y][x]
    cache[y][x] = 0
    o = adj[y][x]
    d = OPER[o]
    ny = y + dy[d]
    nx = x + dx[d]
    cache[y][x] = dfs(ny, nx)
    return cache[y][x]


for i in range(N):
    for j in range(M):
        dfs(i, j)

answer = 0
for i in range(N):
    for j in range(M):
        answer += cache[i][j]
print(answer)
