# BOJ 3079 입국심사

import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline


def check(mid):
    cnt = 0
    for i in range(n):
        cnt += mid // arr[i]
    return True if cnt >= m else False


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
start = 1
end = arr[-1] * m
answer = 0

while start <= end:
    mid = (start + end) // 2
    if check(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)