# BOJ 17825 (주사위 윷놀이)
import sys

sys.stdin = open("input.txt", "r")
si = sys.stdin.readline
jump = [
    [0, 1, 2, 3, 4, 5],  # 0
    [2, 2, 3, 4, 5, 9],  # 1
    [4, 3, 4, 5, 9, 10],  # 2
    [6, 4, 5, 9, 10, 11],  # 3
    [8, 5, 9, 10, 11, 12],  # 4
    [10, 6, 7, 8, 20, 29],  # 5
    [13, 7, 8, 20, 29, 30],  # 6
    [16, 8, 20, 29, 30, 31],  # 7
    [19, 20, 29, 30, 31, 32],  # 8
    [12, 10, 11, 12, 13, 14],  # 9
    [14, 11, 12, 13, 14, 15],  # 10
    [16, 12, 13, 14, 15, 16],  # 11
    [18, 13, 14, 15, 16, 17],  # 12
    [20, 18, 19, 20, 29, 30],  # 13
    [22, 15, 16, 17, 24, 25],  # 14
    [24, 16, 17, 24, 25, 26],  # 15
    [26, 17, 24, 25, 26, 27],  # 16
    [28, 24, 25, 26, 27, 28],  # 17
    [22, 19, 20, 29, 30, 31],  # 18
    [24, 20, 29, 30, 31, 32],  # 19
    [25, 29, 30, 31, 32, 32],  # 20
    [26, 20, 29, 30, 31, 32],  # 21
    [27, 21, 20, 29, 30, 31],  # 22
    [28, 22, 21, 20, 29, 30],  # 23
    [30, 23, 22, 21, 20, 29],  # 24
    [32, 26, 27, 28, 31, 32],  # 25
    [34, 27, 28, 31, 32, 32],  # 26
    [36, 28, 31, 32, 32, 32],  # 27
    [38, 31, 32, 32, 32, 32],  # 28
    [30, 30, 31, 32, 32, 32],  # 29
    [35, 31, 32, 32, 32, 32],  # 30
    [40, 32, 32, 32, 32, 32],  # 31
    [0, 32, 32, 32, 32, 32],  # 32
]


def backtrack(idx):
    if idx == 10:
        score = 0
        pos = [0, 0, 0, 0]
        visited = [False] * 33
        for i in range(10):
            horse = horses[i]
            dice_number = dice[i]
            cur_idx = pos[horse]
            if cur_idx == 32:
                return
            visited[cur_idx] = False
            nxt = jump[cur_idx][dice_number]
            if nxt < 32 and visited[nxt]:
                return
            pos[horse] = nxt
            score += jump[nxt][0]
            visited[nxt] = True

        res[0] = max(res[0], score)
        return

    for i in range(4):
        horses.append(i)
        backtrack(idx + 1)
        horses.pop()


dice = list(map(int, si().split()))  # 말의 index
horses = []
res = [0]
backtrack(0)
print(res[0])
