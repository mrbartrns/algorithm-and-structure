import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n = int(si())
arr = [int(si()) for _ in range(n)]
print(arr)