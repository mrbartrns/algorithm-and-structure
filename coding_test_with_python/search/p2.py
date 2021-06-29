# 떡볶이 떡 만들기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def get_sum(arr, height):
    s = 0
    for i in range(n):
        s += arr[i] - height if arr[i] - height > 0 else 0
    return s


n, m = map(int, si().split())
arr = list(map(int, si().split()))
arr.sort()

start = 0
end = arr[-1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    if get_sum(arr, mid) >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
