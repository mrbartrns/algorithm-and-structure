# 지형 이동
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(land, height):
    labels = [[0 for _ in range(len(land))] for _ in range(len(land))]
    label_number = 1
    for i in range(len(land)):
        for j in range(len(land)):
            if labels[i][j] == 0:
                bfs(i, j, labels=labels, land=land, height=height, label_number=label_number)
                label_number += 1
    edges = []
    parents = [i for i in range(label_number)]
    for y in range(len(land)):
        for x in range(len(land)):
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if ny < 0 or ny >= len(land) or nx < 0 or nx >= len(land):
                    continue
                if labels[y][x] != labels[ny][nx]:
                    edges.append((labels[y][x], labels[ny][nx], abs(land[ny][nx] - land[y][x])))
    return kruskal(parents, edges)


def kruskal(parents, edges):
    n = len(parents) - 1
    s = 0
    edge = 0
    edges.sort(key=lambda x: x[2])

    for a, b, c in edges:
        if not find_parent(parents, a, b):
            union_parent(parents, a, b)
            edge += 1
            s += c
            if edge == n - 1:
                return s
    return 0


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def find_parent(arr, a, b):
    return get_parent(arr, a) == get_parent(arr, b)


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def bfs(sy, sx, **kwargs):
    que = deque()
    kwargs['labels'][sy][sx] = kwargs['label_number']
    que.append((sy, sx))
    while que:
        y, x = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= len(kwargs['labels']) or nx < 0 or nx >= len(kwargs['labels']):
                continue
            if kwargs['labels'][ny][nx] == 0 and abs(kwargs['land'][ny][nx] - kwargs['land'][y][x]) <= kwargs['height']:
                kwargs['labels'][ny][nx] = kwargs['label_number']
                que.append((ny, nx))


if __name__ == '__main__':
    land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    height = 1
    print(solution(land, height))
