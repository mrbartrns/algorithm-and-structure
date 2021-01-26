# BOJ 1158

from collections import deque
import sys

input = sys.stdin.readline


n, k = map(int, input().split())
que = deque([i for i in range(1, n + 1)])


def solve(que, n, k):
    arr = []
    count = 1
    while que:
        if count == k:
            el = que.popleft()
            arr.append(el)
            count = 1
        else:
            count += 1
            el = que.popleft()
            que.append(el)
    return arr


arr = solve(que, n, k)
string = "<"
string += ", ".join(map(str, arr))
string += ">"

print(string)