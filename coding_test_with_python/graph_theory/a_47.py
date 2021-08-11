import copy
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

init_arr = [list(map(int, si().split())) for _ in range(4)]
fish = [[0, 0, 0] for _ in range(17)]
graph = [[0 for _ in range(4)] for _ in range(4)]
answer = []

# init
for i in range(4):
    for j in range(0, 8, 2):
        cur_fish = init_arr[i][j]
        r, c = i, j // 2
        d = init_arr[i][j + 1] - 1
        fish[cur_fish] = [r, c, d]
        graph[r][c] = cur_fish

cur_fish = graph[0][0]
fish[0] = [0, 0, fish[cur_fish][2]]
fish[cur_fish] = [-1, -1, -1]
graph[0][0] = 0
ret = [cur_fish]


def fish_move(fish, graph):
    for i in range(1, 17):
        if fish[i][2] == -1:
            continue
        y, x, d = fish[i]

        for _ in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                d = (d + 1) % 8

            elif graph[ny][nx] == 0:
                d = (d + 1) % 8

            else:
                nxt = graph[ny][nx]
                fish[i] = [ny, nx, d]
                graph[y][x], graph[ny][nx] = nxt, i
                if nxt > 0:
                    fish[nxt][0], fish[nxt][1] = y, x
                break


def shark_move(fish, graph, answer, ret):
    fish_move(fish, graph)
    for i in range(1, 5):
        g = copy.deepcopy(graph)
        f = copy.deepcopy(fish)
        y, x, d = f[0]
        ny = y + dy[d] * i
        nx = x + dx[d] * i

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        if g[ny][nx] == -1:
            continue

        nxt = g[ny][nx]
        g[y][x] = -1
        f[0] = [ny, nx, f[nxt][2]]
        f[nxt] = [-1, -1, -1]
        g[ny][nx] = 0

        ret.append(nxt)
        answer.append(ret[:])
        shark_move(f, g, answer, ret)
        ret.pop()


shark_move(fish, graph, answer, ret)
# print(answer)
res = 0
for ans in answer:
    res = max(res, sum(ans))
print(res)
