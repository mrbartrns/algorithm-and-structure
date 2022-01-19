# BOJ 5582 공통 부분 문자열
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


str1 = si().strip()
str2 = si().strip()
cache = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
max_value = 0

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        max_value = max(max_value, cache[i][j])
print(max_value)
