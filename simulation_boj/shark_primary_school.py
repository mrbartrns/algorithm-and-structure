# BOJ 21608
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def check_vacancy(my, q):
    for y in range(n):
        for x in range(n):
            if graph[y][x] > 0:
                mate = -1
                vac = -1
                heapq.heappush(q, (-mate, -vac, y, x))
            else:
                mate = 0
                vac = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if graph[ny][nx] > 0 and graph[ny][nx] in table[my]:
                        mate += 1
                    elif graph[ny][nx] == 0:
                        vac += 1
                heapq.heappush(q, (-mate, -vac, y, x))


def get_satisfaction_point():
    res = 0
    for y in range(n):
        for x in range(n):
            me = graph[y][x]
            cur = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if graph[ny][nx] in table[me]:
                    cur += 1
            if cur > 0:
                res += 10 ** (cur - 1)
    return res


n = int(si())
friends = []
table = [set() for _ in range(n ** 2 + 1)]
graph = [[0 for _ in range(n)] for _ in range(n)]
# for문 내부로 들어감


for _ in range(n ** 2):
    a, b, c, d, e = map(int, si().split())
    friends.append(a)
    table[a].add(b)
    table[a].add(c)
    table[a].add(d)
    table[a].add(e)

for i in range(n ** 2):
    info = []
    me = friends[i]
    check_vacancy(me, info)
    _, _, row, col = heapq.heappop(info)
    graph[row][col] = me
    # for j in range(n):
    #     for k in range(n):
    #         print(graph[j][k], end=" ")
    #     print()
    # print()

print(get_satisfaction_point())
