# BOJ 1339
import sys

si = sys.stdin.readline

n = int(si())
words = [si().strip() for _ in range(n)]
alphabets = [0] * 26
s = 0
for word in words:
    po = 1
    for i in range(len(word) - 1, -1, -1):
        od = ord(word[i]) - ord("A")
        alphabets[od] += po
        po *= 10

alphabets.sort(reverse=True)
for i in range(len(alphabets)):
    if 9 - i < 0:
        break
    s += (9 - i) * alphabets[i]

print(s)