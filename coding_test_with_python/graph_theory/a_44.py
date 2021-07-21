# BOJ 2887 행성 터널
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = [list(map(int, si().split())) for _ in range(n)]
# print(arr)

arr.sort(key=lambda x: (x[0], x[1], x[2]))
print(arr)
