# BOJ 19236
import copy
import sys

si = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

fish = [0] * 17

graph = []
for i in range(4):
    arr = list(map(int, si().split()))
    temp = []
    for i in range(0, 8, 2):
        temp.append(arr[i])
        fish[arr[i]] = arr[i + 1] - 1
    graph.append(temp)


# graph = [[7, 2, 15, 9],
#          [3, 1, 14, 10],
#          [6, 13, 4, 11],
#          [16, 8, 5, 12]]
# fish = [0, 7, 2, 0, 2, 1, 0, 5, 6, 7, 0, 3, 1, 5, 6, 5, 0]
location = [[-1, -1] for _ in range(17)]
cnt = [0]
catch = []

# 상어가 0, 0으로 들어가 물고기를 먹고 방향을 가짐
fish[0] = fish[graph[0][0]]
fish[graph[0][0]] = -1
catch.append(graph[0][0])
graph[0][0] = 0

# 물고기들의 좌표를 저장
for i in range(4):
    for j in range(4):
        location[graph[i][j]] = [i, j]


def fish_move(maps, directions, locations):
    for i in range(1, 17):
        if directions[i] < 0:
            continue
        d = directions[i]
        y, x = locations[i]
        ny = y + dy[d]
        nx = x + dx[d]
        flag = True

        # 문제 없음
        while ny < 0 or ny >= 4 or nx < 0 or nx >= 4 or maps[ny][nx] == 0:
            d = (d + 1) % 8
            if d == directions[i]:
                flag = False
                break
            ny = y + dy[d]
            nx = x + dx[d]

        if flag:
            directions[i] = d
            if maps[ny][nx] > 0:
                cur_fish = maps[ny][nx]
                locations[i], locations[cur_fish] = locations[cur_fish], locations[i]
                maps[y][x], maps[ny][nx] = cur_fish, i
            else:
                locations[i] = [ny, nx]
                maps[y][x], maps[ny][nx] = -1, i


def backtrack(maps, directions, locations):
    flag = False
    for i in range(1, 5):
        copied_maps = copy.deepcopy(maps)
        copied_directions = copy.deepcopy(directions)
        copied_locations = copy.deepcopy(locations)
        fish_move(copied_maps, copied_directions, copied_locations)
        # for j in range(4):
        #     print(copied_maps[j])
        # print()
        y, x = copied_locations[0]
        d = copied_directions[0]
        ny = y + dy[d] * i
        nx = x + dx[d] * i
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue
        if copied_maps[ny][nx] == -1:
            continue

        flag = True
        cur_fish = copied_maps[ny][nx]
        copied_directions[0] = copied_directions[cur_fish]
        copied_directions[cur_fish] = -1
        copied_maps[ny][nx] = 0
        copied_maps[y][x] = -1
        copied_locations[0] = [ny, nx]
        copied_locations[cur_fish] = [-1, -1]
        catch.append(cur_fish)
        # for j in range(4):
        #     print(copied_maps[j])
        # print()

        backtrack(copied_maps, copied_directions, copied_locations)
        catch.pop()

    if not flag:
        cnt[0] = max(cnt[0], sum(catch))
        return


backtrack(graph, fish, location)
print(cnt[0])
