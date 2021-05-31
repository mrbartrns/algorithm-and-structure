# BOJ 2331
import sys

sys.setrecursionlimit(2000)
si = sys.stdin.readline

n, p = map(int, si().split())
visited = [0] * (1000000)
arr = []


def dfs(arr, v, p, visited):
    if visited[v] < 2:
        if v in arr:
            arr.remove(v)
        else:
            arr.append(v)
        visited[v] += 1
        # 10의 자리가 0이 될때까지 나눈다.
        num = 0
        while v > 0:
            x = v // 10
            y = v % 10
            num += y ** p
            v = x
        dfs(arr, num, p, visited)


dfs(arr, n, p, visited)
print(len(arr))
