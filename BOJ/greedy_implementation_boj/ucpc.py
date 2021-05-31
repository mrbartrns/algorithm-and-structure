# BOJ 15904
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

string = si().strip()
res = ["", "", "", ""]
ans = ["U", "C", "P", "C"]
idx = 0
for c in string:
    if idx >= 4:
        break
    if c == ans[idx]:
        res[idx] = c
        idx += 1

if "".join(res) == "UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")
