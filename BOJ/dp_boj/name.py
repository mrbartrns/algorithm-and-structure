# BOJ 15312 이름 궁합
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

table = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
name1 = si().strip()
name2 = si().strip()
dp = []
for i in range(len(name1)):
    dp.append(table[ord(name1[i]) - ord("A")])
    dp.append(table[ord(name2[i]) - ord("A")])

while len(dp) > 2:
    ret = []
    for i in range(len(dp) - 1):
        ret.append((dp[i] + dp[i + 1]) % 10)
    dp = ret
print("".join(list(map(str, dp))))
