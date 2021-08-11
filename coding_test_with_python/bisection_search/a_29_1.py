# BOJ 2110 (공유기 설치)
import sys

sys.stdin = open("../input.txt")
si = sys.stdin.readline


def check(mid):
    cnt = 1
    last = arr[0]
    for i in range(1, n):
        if arr[i] - last >= mid:
            cnt += 1
            last = arr[i]
            if cnt == c:
                return True
    return False


n, c = map(int, si().split())
arr = [int(si()) for _ in range(n)]
arr.sort()


start = 1
end = arr[-1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)