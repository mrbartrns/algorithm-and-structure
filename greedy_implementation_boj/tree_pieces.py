# BOJ 2947
import sys

si = sys.stdin.readline

arr = list(map(int, si().split()))
while True:
    if arr == [1, 2, 3, 4, 5]:
        break
    for i in range(1, 5):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            print(" ".join(list(map(str, arr))))
