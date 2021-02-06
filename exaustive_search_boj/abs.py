# BOJ 10819
import sys

si = sys.stdin.readline


def track(arr, visited, k):
    if k == len(arr):
        ans.append(temp[:])  # 이슈에 추가할 것
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])
            track(arr, visited, k + 1)
            temp.pop()
            visited[i] = False


def solve(ans):
    res = 0
    for i in range(len(ans)):
        val = 0
        for j in range(1, len(ans[0])):
            val += abs(ans[i][j] - ans[i][j - 1])
        res = max(res, val)
    return res


n = int(si())
arr = list(map(int, si().split()))
visited = [False] * n
ans = []
temp = []
track(arr, visited, 0)
print(solve(ans))