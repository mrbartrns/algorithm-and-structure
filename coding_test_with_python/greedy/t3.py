# 문자열 뒤집기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

string = si().strip()
chk = [0, 0]
flag = "2"
for c in string:
    if flag != c:
        flag = c
        chk[int(c)] += 1
print(min(chk))
