# 왕실의 나이트
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [2, 2, -2, -2, 1, -1, 1, -1]
dx = [-1, 1, -1, 1, 2, 2, -2, -2]

location = si().strip()
y, x = int(location[1]) - 1, ord(location[0]) - ord('a')

cnt = 0
for i in range(8):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 0 or ny >= 8 or nx < 0 or nx >= 8:
        continue
    cnt += 1

print(cnt)
