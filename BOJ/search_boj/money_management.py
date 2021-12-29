# BOJ 6236 용돈 관리
"""
N일 동안 자신이 사용할 금액 계산, 정확히 M번만 통장에서 돈을 빼서 쓴다.
통장에서 K원을 인출한다. 남은 금액이 그 날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원 인출
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 1000000000


def check(mid):
    count = 1
    left = mid
    for i in range(N):
        if arr[i] > mid:
            return False
        if left >= arr[i]:
            left -= arr[i]
        else:
            left = mid - arr[i]
            count += 1
    if count <= M:
        return True
    return False


N, M = map(int, si().strip().split(" "))
arr = []
start = 1
end = INF
for _ in range(N):
    value = int(si().strip())
    arr.append(value)
answer = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
