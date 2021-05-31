# BOJ 10825
import sys

input = sys.stdin.readline


def solve(arr):
    new_arr = list(
        map(lambda x: x[0], sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0])))
    )
    return new_arr


n = int(input())
arr = []
for _ in range(n):
    temp = list(input().split())
    arr.append(temp)

# arr = [["Junkyu", 50, 60, 100], ["Sangkeun", 80, 60, 50], ["Sunyoung", 80, 70, 100]]
arr = list(map(lambda x: [x[0], int(x[1]), int(x[2]), int(x[3])], arr))
new_arr = solve(arr)
for i in range(len(new_arr)):
    print(new_arr[i])