# BOJ 1038 감소하는 수
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def backtrak(idx, n, string):
    if idx == n:
        arr.append(int("".join(string)))
        return
    for i in range(10):
        if (string and int(string[-1]) > i) or not string:
            string.append(str(i))
            backtrak(idx + 1, n, string)
            string.pop()
        else:
            break


arr = []
cnt = 1
while True:
    backtrak(0, cnt, [])
    if arr[-1] == 9876543210:
        break
    cnt += 1
N = int(si())
print(arr[N] if N < len(arr) else -1)
