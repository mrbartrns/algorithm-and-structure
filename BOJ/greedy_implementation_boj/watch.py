# BOJ 15683
import copy
import sys

si = sys.stdin.readline

MAX = 8
INF = 987654321

move = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # right, up, left, down


def blind_spot(room):
    res = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                res += 1
    return res


def dfs(cnt):
    if cnt == len(camera):
        copy_room = copy.deepcopy(graph)
        for i in range(len(angle)):
            y = camera[i][0]
            x = camera[i][1]
            for j in range(4):
                if visited[y][x][j]:
                    # 각도를 바꾼 상태에서 비추기
                    ny = y + move[(angle[i] + j) % 4][0]
                    nx = x + move[(angle[i] + j) % 4][1]
                    while True:
                        if ny < 0 or ny >= n or nx < 0 or nx >= m:
                            break
                        if copy_room[ny][nx] == 6:
                            break
                        if copy_room[ny][nx] == 0:
                            copy_room[ny][nx] = -1
                        ny += move[(angle[i] + j) % 4][0]
                        nx += move[(angle[i] + j) % 4][1]
        res[0] = min(res[0], blind_spot(copy_room))
        return
    for i in range(4):
        angle.append(i)
        dfs(cnt + 1)
        angle.pop()


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
camera = []
angle = []
visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]  # 해당 방향으로 비출것인지에 대한 배열
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

res = [INF]
dfs(0)
print(res[0])
