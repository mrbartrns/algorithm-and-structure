# BOJ 18808
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def rotate(sticker):
    height, width = len(sticker), len(sticker[0])
    rotated_sticker = []
    for x in range(width):
        temp = []
        for y in range(height - 1, -1, -1):
            temp.append(sticker[y][x])
        rotated_sticker.append(temp)
    return rotated_sticker


def check(start_y, start_x, sticker):
    height, width = len(sticker), len(sticker[0])
    for y in range(height):
        for x in range(width):
            if start_y + y < 0 or start_y + y >= n or start_x + x < 0 or start_x + x >= m:
                return False
            if sticker[y][x] == 1 and graph[start_y + y][start_x + x] == 1:
                return False
    return True


def attach(start_y, start_x, sticker):
    height, width = len(sticker), len(sticker[0])
    for y in range(height):
        for x in range(width):
            if sticker[y][x] == 1:
                graph[start_y + y][start_x + x] = 1


# 기본 정보
n, m, k = map(int, si().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
stickers = []
res = 0
for _ in range(k):
    sticker_height, sticker_width = map(int, si().split())
    new_sticker = [list(map(int, si().split())) for _ in range(sticker_height)]
    stickers.append(new_sticker)

for st in stickers:
    sticker = st
    flag = False
    cnt = 0
    while cnt < 4:
        for i in range(n):
            for j in range(m):
                if check(i, j, sticker):
                    attach(i, j, sticker)
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        sticker = rotate(sticker)
        cnt += 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res += 1
print(res)
