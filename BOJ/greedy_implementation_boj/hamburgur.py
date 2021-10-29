# BOJ 19941 햄버거
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N, M = map(int, si().split(" "))


def solve(arr, visited):
    ret = 0
    for i in range(N):
        if arr[i] == "P" and not visited[i]:
            for j in range(i - M, i + M + 1):
                if j < 0 or j >= N:
                    continue
                if arr[j] == "H" and not visited[j]:
                    visited[j] = True
                    visited[i] = True
                    ret += 1
                    break
    return ret


arr = list(si().strip())
visited = [False] * N
answer = solve(arr, visited)
print(answer)
