# BOJ 13325 이진 트리
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def solve(node):
    if cache[node] > -1:
        return cache[node]
    leaf = True
    left = 0
    right = 0
    if node * 2 + 1 < len(cache):
        left = solve(node * 2 + 1) + distance[node * 2]
        leaf = False
    if node * 2 + 2 < len(cache):
        right = solve(node * 2 + 2) + distance[node * 2 + 1]
        leaf = False
    if not leaf and left < right:
        distance[node * 2] += right - left
    elif not leaf and left >= right:
        distance[node * 2 + 1] += left - right
    cache[node] = max(left, right)
    if leaf:
        return 0
    return cache[node]


K = int(si().strip())
distance = list(map(int, si().strip().split(" ")))
cache = [-1] * (2 ** (K + 1) - 1)
solve(0)
print(sum(distance))
