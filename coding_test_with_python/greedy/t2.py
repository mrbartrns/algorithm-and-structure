# 곱하기 혹은 더하기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

str_number = si().strip()
s = 0
for c in str_number:
    if s == 0 or int(c) == 0 or s == 1 or int(c) == 1:
        s += int(c)
    else:
        s *= int(c)
print(s)
