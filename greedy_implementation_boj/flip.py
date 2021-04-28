# BOJ 1439
import sys

# sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

string = si().strip()
idx = -1
arr = [0, 0]
for c in string:
    if int(c) != idx:
        idx = int(c)
        arr[idx] += 1

val = arr.index(max(arr))
cnt = 0
i = 0
while i < len(string):
    flag = False
    while i < len(string) and int(string[i]) != val:
        flag = True
        i += 1

    if flag:
        cnt += 1
    i += 1

print(cnt)
