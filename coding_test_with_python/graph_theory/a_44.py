# BOJ 2887 행성 터널
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def get_parent(parents, a):
    if parents[a] == a:
        return a
    parents[a] = get_parent(parents, parents[a])
    return parents[a]


def find_parent(parents, a, b):
    return get_parent(parents, a) == get_parent(parents, b)


def union_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal(edges):
    edges.sort(key=lambda x: x[2])
    edge = 0
    tot = 0
    parents = [i for i in range(n)]
    for i in range(len(edges)):
        a, b, c = edges[i]
        if not find_parent(parents, a, b):
            union_parent(parents, a, b)
            tot += c
            edge += 1

        if edge == n - 1:
            break
    return tot


n = int(si())
arr = [list(map(int, si().split())) for _ in range(n)]
graph = []

for i in range(n):
    arr[i].append(i)

s1 = sorted(arr, key=lambda x: x[0])
s2 = sorted(arr, key=lambda x: x[1])
s3 = sorted(arr, key=lambda x: x[2])

for i in range(1, n):
    graph.append((s1[i - 1][3], s1[i][3], abs(s1[i - 1][0] - s1[i][0])))
    graph.append((s2[i - 1][3], s2[i][3], abs(s2[i - 1][1] - s2[i][1])))
    graph.append((s3[i - 1][3], s3[i][3], abs(s3[i - 1][2] - s3[i][2])))

print(kruskal(graph))
