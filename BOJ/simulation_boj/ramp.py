# BOJ 14890
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, l = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]


# 한줄씩 검사
def check(route, bridge):
    ramp = bridge[:]
    idx = 0
    h = route[idx]
    idx += 1
    while idx < n:
        if route[idx] - h == 0:
            pass
        elif route[idx] - h == -1:
            i = 0
            while i < l:
                if idx + i >= n:
                    return [-1] * n

                if route[idx + i] != route[idx]:
                    return [-1] * n
                ramp[idx + i] += 1
                i += 1
            idx += i - 1
            h = route[idx]

        elif route[idx] - h == 1:
            i = -l
            while idx + i < idx:
                if idx + i < 0:
                    return [-1] * n
                if route[idx - 1] != route[idx + i]:
                    return [-1] * n
                ramp[idx + i] += 1
                i += 1
            h = route[idx]
        else:
            return [-1] * n
        idx += 1
    for i in range(n):
        if ramp[i] >= 2:
            return [-1] * n
    return ramp


res = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
# 가로 체크
for i in range(n):
    new_ramp = check(graph[i], visited[i])
    if new_ramp[0] > -1:
        for j in range(n):
            visited[i][j] = new_ramp[j]
        res += 1

# 세로 체크
visited = [[0 for _ in range(n)] for _ in range(n)]
for j in range(n):
    temp = [0] * n
    temp_visited = [0] * n
    for i in range(n):
        temp[i] = graph[i][j]
        temp_visited[i] = visited[i][j]
    new_ramp = check(temp, temp_visited)
    if new_ramp[0] > -1:
        for k in range(n):
            visited[k][j] = new_ramp[k]
        res += 1

print(res)
