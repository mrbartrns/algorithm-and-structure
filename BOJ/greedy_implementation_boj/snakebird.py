# BOJ 16435 스네이크버드
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


N, L = map(int, si().split(" "))
arr = list(map(int, si().split(" ")))
arr.sort()
length = L
for c in arr:
    if length < c:
        break
    length += 1
print(length)
