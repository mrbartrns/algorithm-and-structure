# BOJ 2637 장난감 조립
"""
기본 부품 1, 2, 3, 4가 있다.
중간 부품 5는 2개의 기본 부품 1과 1개의 기본 부품 2로 만들어진다.
N -> N - 1까지는 기본부품 또는 중간 부품을 나타내고, N은 완제품을 나타냄
X, Y, K => 중간부품이나 완제품 Y가 K개 필요
adj = [[], [], [], [], [], [(1, 2), (2, 2)], [(5, 2), (3, 3), (4, 4)], [(5, 2), (6, 3), (4, 5)]]
indegree = [0, 1, 1, 1, 2, 2, 1, 0]
counts = [0, 0, 0, 9, 17, 8, 3, 1]
1. 위상정렬을 위하여 indegree 배열 생성 및 인접 행렬 정보 만들기
2. 각 개수를 저장하기 위하여 counts 배열 생성
3. 위상정렬 실시
"""
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def topological_sort():
    q = deque()
    counts[N] = 1
    q.append((N, 1))
    while q:
        node, count = q.popleft()
        for nxt, nxt_count in adj[node]:
            counts[nxt] += nxt_count * count
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append((nxt, counts[nxt]))


N = int(si())
M = int(si())
indegree = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
counts = [0] * (N + 1)
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    adj[a].append((b, c))
    indegree[b] += 1

topological_sort()
for i in range(1, N):
    if adj[i]:
        continue
    print(i, counts[i])
