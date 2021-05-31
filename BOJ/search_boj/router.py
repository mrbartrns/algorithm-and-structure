# BOJ 2110
# 기존 이분탐색에서 하나의 함수가 더 필요 > 놓을 수 있는 공유기의 갯수를 구하는
import sys

si = sys.stdin.readline


n, m = map(int, si().split())
arr = []
for _ in range(n):
    arr.append(int(si()))

# n, m = 5, 3
# arr = [1, 2, 8, 4, 9]
arr.sort()
MIN = 1
MAX = arr[-1] - MIN


def get_count(gap):
    cnt = 1
    last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - last >= gap:
            last = arr[i]
            cnt += 1
    return cnt


def search(start, end, target):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = get_count(mid)
        if cnt < target:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    return res


print(search(MIN, MAX, m))