# 지형 이동
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(land, height):
    labels = [[0 for _ in range(len(land))] for _ in range(len(land))]
    label_number = 1
    for y in range(len(land)):
        for x in range(len(land)):
            if labels[y][x] == 0:
                bfs(y, x, label_number, labels, land, height)
                label_number += 1
    edges = []
    for y in range(len(land)):
        for x in range(len(land)):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= len(land) or nx < 0 or nx >= len(land):
                    continue

                if labels[y][x] != labels[ny][nx]:
                    edges.append((labels[y][x], labels[ny][nx], abs(land[ny][nx] - land[y][x])))
    return kruskal(edges, label_number - 1)


def kruskal(edges, nodes):
    edge = 0
    s = 0
    parents = [i for i in range(nodes + 1)]
    edges.sort(key=lambda x: x[2])
    for a, b, c in edges:
        if get_parent(parents, a) != get_parent(parents, b):
            union_parent(parents, a, b)
            s += c
            edge += 1
        if edge == nodes - 1:
            break
    return s


def get_parent(parents, a):
    if parents[a] == a:
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


def bfs(sy, sx, k, labels, land, height):
    que = deque()
    labels[sy][sx] = k
    que.append((sy, sx))
    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(land) or nx < 0 or nx >= len(land):
                continue

            if abs(land[ny][nx] - land[y][x]) > height:
                continue

            if labels[ny][nx] == 0:
                labels[ny][nx] = k
                que.append((ny, nx))


if __name__ == '__main__':
    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    height = 1
    print(solution(land, height))
