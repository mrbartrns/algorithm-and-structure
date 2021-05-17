# BOJ 15683 (감시)
import copy
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
INF = 987654321


def backtrack(idx, k):
    if idx == k:
        maps = copy.deepcopy(graph)
        for i in range(k):
            y, x = camera[i]
            for d in range(4):
                if visited[y][x][d]:  # y, x 값을 바꾸면 완전히 값이 틀어질 수 있다 -> 4바퀴를 돌아야하는데 y, x값이 계속 갱신되면 위치가 틀어짐
                    ny = y + dy[(d + angle[i]) % 4]
                    nx = x + dx[(d + angle[i]) % 4]
                    while True:
                        if ny < 0 or nx < 0 or ny >= n or nx >= m:
                            break
                        if maps[ny][nx] == 6:
                            break

                        maps[ny][nx] = "#"
                        ny += dy[(d + angle[i]) % 4]
                        nx += dx[(d + angle[i]) % 4]
        cnt = check(maps)
        res[0] = min(cnt, res[0])
        return

    for i in range(4):
        angle.append(i)
        backtrack(idx + 1, k)
        angle.pop()


def check(maps):
    cnt = 0
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0:
                cnt += 1
    return cnt


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
camera = []
angle = []
res = [INF]
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 6:
            camera.append((i, j))
            if graph[i][j] == 1:
                visited[i][j][0] = True
            elif graph[i][j] == 2:
                visited[i][j][0] = True
                visited[i][j][2] = True
            elif graph[i][j] == 3:
                visited[i][j][0] = True
                visited[i][j][1] = True
            elif graph[i][j] == 4:
                visited[i][j][0] = True
                visited[i][j][1] = True
                visited[i][j][2] = True
            elif graph[i][j] == 5:
                visited[i][j][0] = True
                visited[i][j][1] = True
                visited[i][j][2] = True
                visited[i][j][3] = True

backtrack(0, len(camera))
print(res[0])
