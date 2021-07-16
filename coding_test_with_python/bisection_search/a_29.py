import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def check(mid, arr):
    last = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] - last >= mid:
            cnt += 1
            last = arr[i]

    if cnt >= m:
        return True
    return False


n, m = map(int, si().split())
arr = [int(si()) for _ in range(n)]
arr.sort()
start = 1
end = arr[-1] - arr[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    if check(mid, arr):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
