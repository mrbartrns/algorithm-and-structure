import sys


def collatz(n, arr):
    if n == 1:
        arr.append(n)
    else:
        arr.append(n)
        if n % 2 == 0:
            collatz(n // 2, arr)
        else:
            collatz(3 * n + 1, arr)


"""
a, b = map(int, sys.stdin.readline().split())
current = 0
cur_len = 0
for y in range(a, b + 1):
    if y != 2 or y % 2 == 0:
        arr = []
        collatz(y, arr)
        if cur_len < len(arr):
            current = y
            cur_len = len(arr)
        print(y, len(arr))
# print(current, cur_len)
"""


def collatz_memo(n, arr):
    if n < len(arr) and arr[n] != 0:
        return arr[n]
    if n == 1:
        arr[n] = 1
        return arr[1]
    else:
        if n % 2 == 0:
            if n < len(arr):
                arr[n] = collatz_memo(n // 2, arr) + 1
                return arr[n]
                # return arr[n]  # return arr[n]을 해야하는 이유는 이전 스택에서 이 값을 그대로 써야하기 때문임
            else:
                val = collatz_memo(n // 2, arr) + 1
                return val
        else:
            if n < len(arr):
                arr[n] = collatz_memo(3 * n + 1, arr) + 1
                return arr[n]
            else:
                val = collatz_memo(3 * n + 1, arr) + 1
                return val


a, b = map(int, sys.stdin.readline().split())
arr = [0] * 10000001
f = open("answer_arr.txt", "w")
for i in range(a, b + 1):
    collatz_memo(i, arr)

data = "["
for j in arr:
    data += str(j)
    data += ","
data += "]"
f.write(data)
f.close()
