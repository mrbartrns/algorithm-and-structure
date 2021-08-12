# 지형 이동
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(land, height):
    label_table = [[0 for _ in range(len(land))] for _ in range(len(land))]
    label = 1
    for y in range(len(land)):
        for x in range(len(land)):
            if not label_table[y][x]:
                bfs(y, x, label_table, label, land, height)
                label += 1

    edges = []
    for y in range(len(land)):
        for x in range(len(land)):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= len(land) or nx < 0 or nx >= len(land):
                    continue

                cur = label_table[y][x]
                nxt = label_table[ny][nx]
                if cur < nxt:
                    edges.append((cur, nxt, abs(land[ny][nx] - land[y][x])))

    return kruskal(edges, label - 1)


def kruskal(edges, label_counts):
    edge = 0
    answer = 0
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(label_counts + 1)]
    for a, b, c in edges:
        if get_parent(parents, a) != get_parent(parents, b):
            union_parent(parents, a, b)
            answer += c
            edge += 1
            if edge == label_counts - 1:
                return answer
    return 0


def get_parent(parents, a):
    if a == parents[a]:
        return a
    parents[a] = get_parent(parents, parents[a])
    return parents[a]


def union_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def bfs(y, x, label_table, label, land, height):
    que = deque()
    label_table[y][x] = label
    que.append((y, x))
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(label_table) or nx < 0 or nx >= len(label_table):
                continue

            if not label_table[ny][nx] and abs(land[y][x] - land[ny][nx]) <= height:
                label_table[ny][nx] = label
                que.append((ny, nx))


if __name__ == '__main__':
    land = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    height = 3
    print(solution(land, height))
