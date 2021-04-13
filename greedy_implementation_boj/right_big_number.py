# BOJ 17298
import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
# n = 11
# arr = [1, 10, 999999, 7, 999998, 3, 1, 4, 1000000, 3, 1000000]
stack = []
ret = [-1] * n
top = arr[-1]

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        ret[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)

print(" ".join(list(map(str, ret))))
