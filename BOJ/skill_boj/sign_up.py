import sys

input = sys.stdin.readline

# arr = [[21, "JunKyuddddddddddd"], [21, "Dohyun"], [20, "Sunyoung"]]


def solve(arr):
    arr.sort(key=lambda x: x[0])
    return arr


# print(arr)
n = int(input())
arr = []
for _ in range(n):
    temp = list(input().split())
    arr.append(temp)

arr = list(map(lambda x: [int(x[0]), x[1]], arr))
new_arr = solve(arr)
for i in range(len(new_arr)):
    print(" ".join(list(map(str, arr[i]))))