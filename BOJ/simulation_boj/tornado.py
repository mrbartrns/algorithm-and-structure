# BOJ 20057
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
tornado = [[False for _ in range(n)] for _ in range(n)]
st = (n // 2, n // 2)


# 토네이도의 이동 먼저 구현
def move(y, x, d, scale):
    t = 0
    tornado[y][x] = True
    while t < scale:
        ny = y + dy[d]
        nx = x + dx[d]
        if not tornado[ny][nx]:
            tornado[ny][nx] = True
            y, x = ny, nx
            # ret[0] += spread(y, x, d)
            # for i in range(n):
            #     for j in range(n):
            #         print(graph[i][j], end=" ")
            #     print()
            # print()
        t += 1
    return y, x


def spread(y, x, d):
    # 현재 칸의 모든 모래가 사라져야함
    silicon = graph[y][x]
    # print(silicon)
    outer_scope = 0
    s = 0
    right = (d + 3) % 4
    left = (d + 1) % 4
    # right check
    if y + dy[right] < 0 or y + dy[right] >= n or x + dx[right] < 0 or x + dx[right] >= n:
        outer_scope += silicon * 7 // 100
    else:
        graph[y + dy[right]][x + dx[right]] += silicon * 7 // 100
    s += silicon * 7 // 100

    if y + 2 * dy[right] < 0 or y + 2 * dy[right] >= n or x + 2 * dx[right] < 0 or x + 2 * dx[right] >= n:
        outer_scope += silicon * 2 // 100
    else:
        graph[y + 2 * dy[right]][x + 2 * dx[right]] += silicon * 2 // 100
    s += silicon * 2 // 100

    # left check
    if y + dy[left] < 0 or y + dy[left] >= n or x + dx[left] < 0 or x + dx[left] >= n:
        outer_scope += silicon * 7 // 100
    else:
        graph[y + dy[left]][x + dx[left]] += silicon * 7 // 100
    s += silicon * 7 // 100

    if y + 2 * dy[left] < 0 or y + 2 * dy[left] >= n or x + 2 * dx[left] < 0 or x + 2 * dx[left] >= n:
        outer_scope += silicon * 2 // 100
    else:
        graph[y + 2 * dy[left]][x + 2 * dx[left]] += silicon * 2 // 100
    s += silicon * 2 // 100

    # front check
    if y + 2 * dy[d] < 0 or y + 2 * dy[d] >= n or x + 2 * dx[d] < 0 or x + 2 * dx[d] >= n:
        outer_scope += silicon * 5 // 100
    else:
        graph[y + 2 * dy[d]][x + 2 * dx[d]] += silicon * 5 // 100
    s += silicon * 5 // 100

    # check else
    if d == 0:
        if y + dy[right] < 0 or y + dy[right] >= n or x + dx[right] - 1 < 0 or x + dx[right] - 1 >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[right]][x + dx[right] - 1] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[right] < 0 or y + dy[right] >= n or x + dx[right] + 1 < 0 or x + dx[right] + 1 >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[right]][x + dx[right] + 1] += silicon * 1 // 100
        s += silicon * 1 // 100

        if y + dy[left] < 0 or y + dy[left] >= n or x + dx[left] - 1 < 0 or x + dx[left] - 1 >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[left]][x + dx[left] - 1] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[left] < 0 or y + dy[left] >= n or x + dx[left] + 1 < 0 or x + dx[left] + 1 >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[left]][x + dx[left] + 1] += silicon * 1 // 100
        s += silicon * 1 // 100
    elif d == 1:
        if y + dy[right] + 1 < 0 or y + dy[right] + 1 >= n or x + dx[right] < 0 or x + dx[right] >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[right] + 1][x + dx[right]] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[right] - 1 < 0 or y + dy[right] - 1 >= n or x + dx[right] < 0 or x + dx[right] >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[right] - 1][x + dx[right]] += silicon * 1 // 100
        s += silicon * 1 // 100

        if y + dy[left] + 1 < 0 or y + dy[left] + 1 >= n or x + dx[left] < 0 or x + dx[left] >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[left] + 1][x + dx[left]] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[left] - 1 < 0 or y + dy[left] - 1 >= n or x + dx[left] < 0 or x + dx[left] >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[left] - 1][x + dx[left]] += silicon * 1 // 100
        s += silicon * 1 // 100

    elif d == 2:
        if y + dy[right] < 0 or y + dy[right] >= n or x + dx[right] + 1 < 0 or x + dx[right] + 1 >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[right]][x + dx[right] + 1] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[right] < 0 or y + dy[right] >= n or x + dx[right] - 1 < 0 or x + dx[right] - 1 >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[right]][x + dx[right] - 1] += silicon * 1 // 100
        s += silicon * 1 // 100

        if y + dy[left] < 0 or y + dy[left] >= n or x + dx[left] + 1 < 0 or x + dx[left] + 1 >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[left]][x + dx[left] + 1] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[left] < 0 or y + dy[left] >= n or x + dx[left] - 1 < 0 or x + dx[left] - 1 >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[left]][x + dx[left] - 1] += silicon * 1 // 100
        s += silicon * 1 // 100

    elif d == 3:
        if y + dy[right] - 1 < 0 or y + dy[right] - 1 >= n or x + dx[right] < 0 or x + dx[right] >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[right] - 1][x + dx[right]] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[right] + 1 < 0 or y + dy[right] + 1 >= n or x + dx[right] < 0 or x + dx[right] >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[right] + 1][x + dx[right]] += silicon * 1 // 100
        s += silicon * 1 // 100

        if y + dy[left] - 1 < 0 or y + dy[left] - 1 >= n or x + dx[left] < 0 or x + dx[left] >= n:
            outer_scope += silicon * 10 // 100
        else:
            graph[y + dy[left] - 1][x + dx[left]] += silicon * 10 // 100
        s += silicon * 10 // 100

        if y + dy[left] + 1 < 0 or y + dy[left] + 1 >= n or x + dx[left] < 0 or x + dx[left] >= n:
            outer_scope += silicon * 1 // 100
        else:
            graph[y + dy[left] + 1][x + dx[left]] += silicon * 1 // 100
        s += silicon * 1 // 100
    # s = silicon * 45 // 100
    if y + dy[d] < 0 or y + dy[d] >= n or x + dx[d] < 0 or x + dx[d] >= n:
        outer_scope += silicon - s
    else:
        graph[y + dy[d]][x + dx[d]] += silicon - s
    # print(outer_scope)
    graph[y][x] = 0

    return outer_scope


r, c = st
d = 0
scale = 1
ret = [0]
# while True:
#     r, c = move(r, c, d, scale)
#     print(r, c)
#     if r == 0 and c == 0:
#         break
#     d = (d + 1) % 4
#     if d % 2 == 0:
#         scale += 1
#     print(scale)
# print(ret[0])
r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)

r, c = move(r, c, d, scale)
print(r, c)
d = (d + 1) % 4
if d % 2 == 0:
    scale += 1
print(scale)


