# 문자열 재정렬
import sys

# sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

string = si().strip()
alphabets = []
number = 0
for c in string:
    if "0" <= c <= "9":
        number += int(c)
    else:
        alphabets.append(c)
alphabets.sort()
ret = "".join(alphabets) + str(number)
print(ret)
