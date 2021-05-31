# BOJ 15683
import copy
import sys

move_dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
si = sys.stdin.readline


def dfs(cnt):
    size = len(camera)
    copy_room = copy.deepcopy(graph)
    if cnt == size:
        for i in range(size):
            y, x = camera[i]
            for j in range(4):
                if visited[y][x][j]:
                    # 현재 좌표는 카메라이므로 다음 좌표부터 실행
                    ny = y + move_dir[(angle[i] + j) % 4][0]
                    nx = x + move_dir[(angle[i] + j) % 4][1]
                    while True:
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            break
                        if copy_room[ny][nx] == 6:
                            break
                        if copy_room[ny][nx] == 0:
                            copy_room[nx][ny] = -1
                        ny += move_dir[(angle[i] + j) % 4][0]
                        nx += move_dir[(angle[i] + j) % 4][1]
        res[0] = min(res[0], blind_spot(copy_room))
        return
    for d in range(4):
        angle.append(d)
        dfs(cnt + 1)
        angle.pop()


def blind_spot(maps):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                cnt += 1
    return cnt


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
camera = []
angle = []
res = [987654321]

for j in range(n):
    for i in range(m):
        if 0 < graph[j][i] < 6:
            camera.append((j, i))

        if graph[j][i] == 1:
            visited[j][i][0] = True
        elif graph[j][i] == 2:
            visited[j][i][0] = True
            visited[j][i][2] = True
        elif graph[j][i] == 3:
            visited[j][i][0] = True
            visited[j][i][1] = True
        elif graph[j][i] == 4:
            visited[j][i][0] = True
            visited[j][i][1] = True
            visited[j][i][2] = True
        elif graph[j][i] == 5:
            visited[j][i][0] = True
            visited[j][i][1] = True
            visited[j][i][2] = True
            visited[j][i][3] = True

dfs(0)
print(res[0])
