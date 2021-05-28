# BOJ 20608 (상어 초등학교)
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def get_location(me):
    q = []
    for y in range(n):
        for x in range(n):
            if graph[y][x] > 0:
                continue
            my_friend = 0
            blank = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if graph[ny][nx] == 0:
                    blank += 1

                elif graph[ny][nx] in friends[me]:
                    my_friend += 1
            heapq.heappush(q, (-my_friend, -blank, y, x))
    if q:
        _, _, y, x = heapq.heappop(q)
        return y, x


def get_satisfaction_score():
    s = 0
    for y in range(n):
        for x in range(n):
            t = 0
            me = graph[y][x]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                my_friend = graph[ny][nx]
                if my_friend in friends[me]:
                    t += 1

            s += 10 ** (t - 1) if t > 0 else 0
    return s


n = int(si())
table = []
friends = [set() for _ in range(n ** 2 + 1)]
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n ** 2):
    a1, a2, a3, a4, a5 = map(int, si().split())
    table.append(a1)
    friends[a1].add(a2)
    friends[a1].add(a3)
    friends[a1].add(a4)
    friends[a1].add(a5)

for student in table:
    r, c = get_location(student)
    graph[r][c] = student

print(get_satisfaction_score())
