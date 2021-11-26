# BOJ 10423 전기가 부족해
"""
발전소를 만들 때 중요한 것은 발전소 건물과 도시로 전기를 공급해줄 케이블
발전소는 이미 특정 도시에 설치되어 있다.
어느 한 도시가 두개의 발전소에서 전기를 공급받으면 낭비 -> 케이블이 연결되어 있는 도시는 반드시 발전소가 하나만 존재
크루스컬 알고리즘인가?
- 모든 도시에 전선을 연결하여 최소 비용으로 연결하는 알고리즘은 크루스컬 알고리즘의 모양은 맞다.
- 다만 주의해야 할 것은 연결된 모든 노드가 하나의 발전소와 연결되어 있어야 한다는 것이다.
1. 크루스컬 알고리즘처럼 두 노드가 연결되어 있지 않을 때, union-find 알고리즘으로 두 노드를 연결후 비용을 더한다.
2. 모든 노드를 연결한다면 N - 1개의 간선으로 N개의 노드를 연결하게 된다. 만약 추가 조건이 주어진다면 연결 노드는 이보다 작다.
3. 발전소가 항상 작은 번호라는 보장이 없으므로 둘 중 하나가 발전소 번호라면 발전소 번호 쪽으로 parent를 붙인다.
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def find(arr, a):
    if a == arr[a]:
        return a
    arr[a] = find(arr, arr[a])
    return arr[a]


def union(arr, a, b):
    a = find(arr, a)
    b = find(arr, b)
    if plant[a]:
        arr[b] = a
    elif plant[b]:
        arr[a] = b
    else:
        if a < b:
            arr[b] = a
        else:
            arr[a] = b


def kruskal():
    parents = [i for i in range(N + 1)]
    ret = 0
    edge_count = 0
    edges.sort(key=lambda x: x[2])
    for a, b, c in edges:
        if plant[find(parents, a)] and plant[find(parents, b)]:
            continue

        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            ret += c
            edge_count += 1

        if edge_count == N - 1:
            break
    return ret


N, M, K = map(int, si().split(" "))
plant = [False] * (N + 1)
ps = list(map(int, si().split(" ")))
for p in ps:
    plant[p] = True
# 발전소가 설치된 도시의 번호
# M개의 전선줄 u, v, w -> (u 도시와 v 도시를 연결하는 케이블을 설치할때 드는 비용)
edges = []
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    edges.append((a, b, c))
print(kruskal())
