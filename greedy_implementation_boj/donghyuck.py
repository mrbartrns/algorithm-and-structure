# BOJ 2720
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

t = int(si())
for _ in range(t):
    arr = [0, 0, 0, 0]
    coins = [25, 10, 5, 1]
    value = int(si())
    for i in range(4):
        arr[i] = value // coins[i]
        value = value - arr[i] * coins[i]
        print(arr[i], end=" ")
    print()
