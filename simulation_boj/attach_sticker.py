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


# 기본 정보
n, m, k = map(int, si().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
stickers = []
for _ in range(k):
    sticker_height, sticker_width = map(int, si().split())
    new_sticker = [list(map(int, si().split())) for _ in range(sticker_height)]
    stickers.append(new_sticker)



# test = rotate(stickers[3])
# for i in range(len(test)):
#     for j in range(len(test[0])):
#         print(test[i][j], end=" ")
#     print()
