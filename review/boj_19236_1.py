# BOJ 19236 (청소년 상어)
import copy
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def rotate(maps: list, locations: list, directions: list):
    """
    rotate and move fish.
    Args:
        maps(list): copied graph
        locations(list): copied locations of fish
        directions(list): copied directions of fish

    Returns: None

    """
    for i in range(1, 17):
        y, x = locations[i]
        d = directions[i]
        if d == -1:
            continue
        t = 0
        while t < 8:
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                d = (d + 1) % 8

            elif maps[ny][nx] == 0:
                d = (d + 1) % 8

            else:
                next_fish = maps[ny][nx]
                locations[i] = [ny, nx]
                if next_fish > -1:
                    locations[next_fish] = [y, x]
                maps[y][x], maps[ny][nx] = maps[ny][nx], maps[y][x]
                directions[i] = d
                break
            t += 1


def backtrack(maps, locations, directions):
    for i in range(1, 4):  # 상어가 움직일 수 있는만큼 백트래킹
        copied_maps = copy.deepcopy(maps)
        copied_locations = copy.deepcopy(locations)
        copied_directions = copy.deepcopy(directions)

        # 물고기가 먼저 이동
        rotate(copied_maps, copied_locations, copied_directions)
        # 상어가 이동하려는 위치 선택
        y, x = copied_locations[0]
        d = copied_directions[0]
        ny = y + dy[d] * i
        nx = x + dx[d] * i
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        if copied_maps[ny][nx] == -1:
            continue

        if copied_maps[ny][nx] > 0:
            next_fish = copied_maps[ny][nx]
            copied_directions[0] = copied_directions[next_fish]
            copied_locations[0] = [ny, nx]
            copied_locations[next_fish] = [-1, -1]
            copied_directions[next_fish] = -1
            copied_maps[y][x] = -1
            copied_maps[ny][nx] = 0
            stash.append(next_fish)
            res[0] = max(res[0], sum(stash))
            backtrack(copied_maps, copied_locations, copied_directions)
            stash.pop()


fish = [[0, 0] for _ in range(17)]
directions = [0] * 17
graph = [[0 for _ in range(4)] for _ in range(4)]
stash = []
res = [0]
# 물고기들을 그래프에 삽입하기
for i in range(4):
    temp = list(map(int, si().split()))
    for j in range(0, 8, 2):
        cur_fish = temp[j]
        graph[i][j // 2] = cur_fish
        directions[cur_fish] = temp[j + 1] - 1

# 위치 배열 초기화
for i in range(4):
    for j in range(4):
        cur_fish = graph[i][j]
        fish[cur_fish] = [i, j]

cur_fish = graph[0][0]
stash.append(cur_fish)
directions[0] = directions[cur_fish]
graph[0][0] = 0
fish[cur_fish] = [-1, -1]
directions[cur_fish] = -1
res[0] += cur_fish

backtrack(graph, fish, directions)
print(res[0])
