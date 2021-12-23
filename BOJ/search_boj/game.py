# BOJ 1072 게임
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

X, Y = map(int, si().strip().split(" "))
INF = int(1e15)


# 실수 자료형은 정확한 수를 저장하지 못한다.
def check(x, y, mid):
    rate = y * 100 // x
    new_rate = (y + mid) * 100 // (x + mid)
    if new_rate > rate:
        return True
    return False


start = 0
end = 1000000000
answer = INF
while start <= end:
    mid = (start + end) // 2
    if check(X, Y, mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer if answer < INF else -1)
