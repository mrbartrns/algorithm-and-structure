# BOJ 9177 단어 섞기
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n = int(si().strip())
cnt = 0
while cnt < n:
    word1, word2, word3 = map(str, si().strip().split(" "))
    cache = [[False for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    cache[0][0] = True  # blank string is always true
    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if i == 0 and j == 0:
                continue
            if word3[i + j - 1] == word1[i - 1]:
                cache[i][j] = cache[i][j] or cache[i - 1][j]
            if word3[i + j - 1] == word2[j - 1]:
                cache[i][j] = cache[i][j] or cache[i][j - 1]
    cnt += 1
    print(
        "Data set {cnt}: {value}".format(
            cnt=cnt, value="yes" if cache[len(word1)][len(word2)] else "no"
        )
    )
