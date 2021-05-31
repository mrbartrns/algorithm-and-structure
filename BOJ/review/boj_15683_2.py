# BOJ 15683 감시
import copy
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
INF = 987654321


def get_blind_spot(maps):
    cnt = 0
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0:
                cnt += 1
    return cnt


def backtrack(idx, k):
    if idx == k:
        maps = copy.deepcopy(graph)
        for i in range(len(camera)):
            y, x = camera[i]
            for d in range(4):
                if visited[y][x][d]:
                    ny = y + dy[(d + angle[i]) % 4]
                    nx = x + dx[(d + angle[i]) % 4]
                    while True:
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            break
                        if maps[ny][nx] == 6:
                            break
                        maps[ny][nx] = -1
                        ny += dy[(d + angle[i]) % 4]
                        nx += dx[(d + angle[i]) % 4]
        res[0] = min(res[0], get_blind_spot(maps))
        return

    for i in range(4):
        angle.append(i)
        backtrack(idx + 1, k)
        angle.pop()


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
camera = []
angle = []
res = [INF]

for r in range(n):
    for c in range(m):
        if 0 < graph[r][c] < 6:
            camera.append((r, c))
            if graph[r][c] == 1:
                visited[r][c][0] = True
            elif graph[r][c] == 2:
                visited[r][c][0] = True
                visited[r][c][2] = True
            elif graph[r][c] == 3:
                visited[r][c][0] = True
                visited[r][c][1] = True
            elif graph[r][c] == 4:
                visited[r][c][0] = True
                visited[r][c][1] = True
                visited[r][c][2] = True
            elif graph[r][c] == 5:
                visited[r][c][0] = True
                visited[r][c][1] = True
                visited[r][c][2] = True
                visited[r][c][3] = True

backtrack(0, len(camera))
print(res[0])
