# BOJ 1543 (문서 검색)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

doc = si().strip()
word = si().strip()

idx = 0
cnt = 0
cur_idx = doc.find(word, idx)
while cur_idx > -1:
    idx = cur_idx + len(word)
    cnt += 1
    cur_idx = doc.find(word, idx)

print(cnt)
