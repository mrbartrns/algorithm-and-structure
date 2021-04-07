# BOJ 15683
import copy
import sys

si = sys.stdin.readline

n, m = map(int, si().split())

move = [[0, 1], [-1, 0], [0, -1], [1, 0]]
INF = 987654321


def blind_spot(room):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                cnt += 1
    return cnt


def dfs(cnt):
    if cnt == len(camera):
        copy_room = copy.deepcopy(graph)
        for i in range(len(camera)):
            x, y = camera[i]
            # j 는 활성화된 move에 대해서만 실행한다는 뜻
            for j in range(4):
                if visited[x][y][j]:
                    nx = x + move[(angle[i] + j) % 4][0]
                    ny = y + move[(angle[i] + j) % 4][1]
                    while True:
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            break
                        if copy_room[nx][ny] == 6:
                            break
                        copy_room[nx][ny] = -1
                        nx += move[(angle[i] + j) % 4][0]
                        ny += move[(angle[i] + j) % 4][1]
        res[0] = min(res[0], blind_spot(copy_room))
        return
    for i in range(4):
        angle.append(i)
        dfs(cnt + 1)
        angle.pop()


camera = []
angle = []
visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
graph = [list(map(int, si().split())) for _ in range(n)]
res = [INF]
# 카메라를 카메라 배열에 넣은 후, 카메라의 종류에 따라서 방향 활성화하기
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 6:
            camera.append((i, j))

            # 첫 방향 정하기
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

dfs(0)
print(res[0])
