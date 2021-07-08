import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(map(int, si().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] != arr[j]:
            cnt += 1
print(cnt)
