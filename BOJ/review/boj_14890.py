# BOJ 14890 (경사로)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def check_ramp(ramp):
    visited = [False] * n
    idx = 0
    height = ramp[0]
    while idx < n:
        if abs(height - ramp[idx]) > 1:
            return False

        if height > ramp[idx]:
            if idx + L > n:
                return False

            i = 0
            while i < L:
                if ramp[idx + i] != ramp[idx]:
                    return False

                if visited[idx + i]:
                    return False

                visited[idx + i] = True
                i += 1

        elif height < ramp[idx]:
            if idx - L < 0:
                return False
            i = -L
            while idx + i < idx:
                if ramp[idx + i] != height:
                    return False

                if visited[idx + i]:
                    return False
                visited[idx + i] = True
                i += 1
        height = ramp[idx]
        idx += 1
    return True


n, L = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(graph[i][j])
    if check_ramp(temp):
        cnt += 1

for j in range(n):
    temp = []
    for i in range(n):
        temp.append(graph[i][j])
    if check_ramp(temp):
        cnt += 1
print(cnt)
