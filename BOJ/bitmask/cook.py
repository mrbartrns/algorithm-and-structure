# BOJ 2961 도영이가 만든 맛있는 음식
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = int(1e12)

n = int(si())
answer = INF
arr = [list(map(int, si().split())) for _ in range(n)]
for i in range(1, 1 << n):
    sour = 1
    bitter = 0
    for j in range(n):
        if i & (1 << j):
            sour *= arr[j][0]
            bitter += arr[j][1]
    answer = min(answer, abs(sour - bitter))
print(answer)