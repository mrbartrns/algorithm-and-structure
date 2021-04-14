# BOJ 1331
import sys

si = sys.stdin.readline

move_dir = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
graph = [[False for _ in range(6)] for _ in range(6)]
routes = []
check = True
# temp = ["A1", "B3", "A5", "C6", "E5", "F3", "D2", "F1", "E3", "F5", "D4", "B5", "A3", "B1", "C3", "A2", "C1", "E2",
#         "F4", "E6", "C5", "A6", "B4", "D5", "F6", "E4", "D6", "C4", "B6", "A4", "B2", "D1", "F2", "D3", "E1", "C2"]
for i in range(36):
    temp = si().strip()
    r = ord(temp[0]) - ord('A')
    c = int(temp[1]) - 1
    # r = ord(temp[i][0]) - ord('A')
    # c = int(temp[i][1]) - 1
    routes.append((r, c))

# print(routes)

for i in range(36):
    flag = False
    y, x = routes[i]
    next_y, next_x = routes[(i + 1) % 36]
    graph[y][x] = True
    for d in range(8):
        dy, dx = move_dir[d]
        ny = y + dy
        nx = x + dx
        if nx < 0 or ny < 0 or nx >= 6 or ny >= 6:
            continue
        if not graph[ny][nx] and ny == next_y and nx == next_x:
            flag = True
            break
        elif i == 35 and next_y == routes[0][0] and next_x == routes[0][1]:
            flag = True

    if not flag:
        check = False
        break

print('Valid' if check else 'Invalid')
