# BOJ 19236 (청소년 상어)
import copy
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def fish_move(idx: int, maps: list, fish_locations: list, fish_directions: list) -> None:
    """
    Move fish to correct location.
    Args:
        idx(int): index of fish
        maps(list): copied_maps
        fish_locations(list): copied fish locations
        fish_directions(list): copied fish directions
    Returns: None

    """
    y, x = fish_locations[idx]
    d = fish_directions[idx]
    t = 0
    while t < 8:
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            d = (d + 1) % 8

        elif maps[ny][nx] == 0:
            d = (d + 1) % 8

        else:
            next_idx = maps[ny][nx]
            fish_directions[idx] = d
            maps[y][x], maps[ny][nx] = maps[ny][nx], maps[y][x]
            fish_locations[idx] = [ny, nx]
            if next_idx > -1:
                fish_locations[next_idx] = [y, x]
            break
        t += 1


def backtrack(maps, fish_locations, fish_directions):
    """
    상어의 움직임을 구현하는 함수
    상어는 -1인 위치로 이동할 수 없으며, 이동한 뒤에는 상어가 원래 있던 위치가 -1로 바뀌어야 한다.

    Args:
        maps(list): copied_maps
        fish_locations(list): copied location of fish
        fish_directions(list): copied direction of fish
    Returns: None

    """
    flag = False
    for i in range(1, 5):
        copied_maps = copy.deepcopy(maps)
        copied_locations = copy.deepcopy(fish_locations)
        copied_directions = copy.deepcopy(fish_directions)
        for j in range(1, 17):
            if copied_directions[j] > -1:
                fish_move(j, copied_maps, copied_locations, copied_directions)

        y, x = copied_locations[0]  # shark location
        d = copied_directions[0]
        ny = y + dy[d] * i
        nx = x + dx[d] * i

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        if copied_maps[ny][nx] == -1:
            continue

        flag = True
        cur_fish = copied_maps[ny][nx]
        # 복사
        copied_directions[0] = copied_directions[cur_fish]
        copied_locations[0] = [ny, nx]
        copied_maps[y][x] = -1
        copied_maps[ny][nx] = 0

        # 갱신
        copied_directions[cur_fish] = -1
        copied_locations[cur_fish] = [-1, -1]
        catch.append(cur_fish)
        backtrack(copied_maps, copied_locations, copied_directions)
        catch.pop()

    if not flag:
        res[0] = max(res[0], sum(catch))


graph = [[0 for _ in range(4)] for _ in range(4)]

directions = [0] * 17  # 0번 물고기는 상어, 방향을 저장하는 배열
locations = [[0, 0] for _ in range(17)]
catch = []

# initialize
for i in range(4):
    temp = list(map(int, si().split()))
    for j in range(0, 8, 2):
        cur_fish = temp[j]
        graph[i][j // 2] = cur_fish
        directions[cur_fish] = temp[j + 1] - 1
        locations[cur_fish] = [i, j // 2]

res = [0]
# 처음에 상어는 0, 0의 위치에 있다
shark_y, shark_x = 0, 0
died = graph[shark_y][shark_x]
directions[0] = directions[died]
directions[died] = -1
graph[shark_y][shark_x] = 0
locations[died] = [-1, -1]
catch.append(died)

backtrack(graph, locations, directions)
print(res[0])
# 물고기를 움직이는 함수
# for i in range(1, 17):
#     if directions[i] > -1:
#         fish_move(i)
