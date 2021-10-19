# BOJ 19939 박 터트리기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N, K = map(int, si().split(" "))
N -= K * (K + 1) // 2
if N < 0:
    print(-1)
elif N % K > 0:
    print(K)
else:
    print(K - 1)
