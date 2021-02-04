# BOJ 11729
import sys

si = sys.stdin.readline


def hanoi(from_, to_, aux_, n):
    if n == 1:
        print(from_, to_)
    # n - 1개를 from-에서 aux_로 보낸다
    else:
        hanoi(from_, aux_, to_, n - 1)
        print(from_, to_)
        # n - 1개를 aux_에서 to_로 보낸다
        hanoi(aux_, to_, from_, n - 1)


n = int(si())
total = 0
# 분할 정복의 기초! 몇번 반복하는지에 대해 정확히 알고 있어야 함
for _ in range(n):
    total *= 2
    total += 1
print(total)
hanoi(1, 3, 2, n)
