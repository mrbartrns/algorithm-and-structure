# 숫자 카드 게임
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n, m = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
res = 0
for i in range(n):
    res = max(min(board[i]), res)
print(res)
