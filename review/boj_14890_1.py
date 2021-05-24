# BOJ 14890 (경사로)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def check_ramp(arr):
    idx = 0
    height = arr[0]
    visited = [False] * n
    while idx < n:
        if abs(arr[idx] - height) > 1:
            return False

        if arr[idx] < height:
            i = 0

            while i < l:
                if idx + i >= n:
                    return False

                if arr[idx] != arr[idx + i]:
                    return False

                if visited[idx + i]:
                    return False

                visited[idx + i] = True
                i += 1

        elif arr[idx] > height:
            i = -l
            while idx + i < idx:
                if idx + i < 0:
                    return False

                if arr[idx + i] != height:
                    return False

                if visited[idx + i]:
                    return False
                visited[idx + i] = True
                i += 1

        height = arr[idx]
        idx += 1
    return True


n, l = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
res = 0

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(graph[i][j])
    if check_ramp(temp):
        res += 1

for j in range(n):
    temp = []
    for i in range(n):
        temp.append(graph[i][j])
    if check_ramp(temp):
        res += 1

print(res)
