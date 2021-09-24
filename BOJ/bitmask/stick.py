# BOJ 1094 막대기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n = int(si())

cnt = 0
for i in range(8):
    if n & (1 << i):
        cnt += 1
print(cnt)