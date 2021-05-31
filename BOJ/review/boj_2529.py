# BOJ 2529
import sys

si = sys.stdin.readline


def backtrack(string, k, n):
    if k == n:
        arr.append(string)
        return
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            if k == 0:
                backtrack(string + str(i), k + 1, n)
            else:
                if sign[k - 1] == "<" and int(string[k - 1]) < i:
                    backtrack(string + str(i), k + 1, n)
                elif sign[k - 1] == ">" and int(string[k - 1]) > i:
                    backtrack(string + str(i), k + 1, n)
            visited[i] = False


arr = []
n = int(si())
sign = list(si().split())
visited = [False] * 10
MAX = -1
MIN = 1e15
MIN_ = ""
MAX_ = ""

backtrack("", 0, n + 1)
for numset in arr:
    temp = int(numset)
    if MIN > temp:
        MIN = temp
        MIN_ = numset
    if MAX < temp:
        MAX = temp
        MAX_ = numset

print(MAX_)
print(MIN_)