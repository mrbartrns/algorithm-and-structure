# BOJ 10825 국영수
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
arr = []
for _ in range(n):
    temp = list(si().strip().split(" "))
    temp[1], temp[2], temp[3] = int(temp[1]), int(temp[2]), int(temp[3])
    arr.append(temp)

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(arr[i][0])
