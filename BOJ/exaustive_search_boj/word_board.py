# BOJ 2186
import sys
from collections import deque

si = sys.stdin.readline

"""
00
이 문자의 한 칸(아무칸에서 상관 없음)에서 시작하여 움직일 수 있다. -> 처음부터 끝까지 순회해 봐야함
움직일때에는 상하좌우로 k개의 칸까지만 이동이 가능 -> dx, dy배열에 k배를 한 값을 이용이 가능
반드시 한 칸 이상 움직여야 함. 같은칸을 여러번 방문 가능 -> visited 배열 불필요
영단어를 만들 수 있는 경로가 몇개 있는지 알아내는 프로그램

주어진 배열의 크기 100 * 100 이고 이것은 백트래킹으로 해결이 불가능한 크기
즉 bfs로 해결이 필요
첫 시작점이 첫글자와 동일할 때, bfs를 시작한다.
"""

# 글자
def bfs(x, y, k, word):
    cnt = 0
    que = deque()
    que.append((x, y, board[x][y]))
    while que:
        x, y, c = que.popleft()

        # 글자의 길이를 초과하면 더이상 탐색할 필요가 없다.
        if len(c) > len(word):
            continue

        if c == word:
            cnt += 1

        for j in range(1, k + 1):
            for i in range(4):
                nx = x + (j * dx[i])
                ny = y + (j * dy[i])

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                que.append((nx, ny, c + board[nx][ny]))
    return cnt


n, m, k = map(int, si().split())
board = []
for _ in range(n):
    board.append(list(si().strip()))

word = si().strip()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            res += bfs(i, j, k, word)

sys.stdout.write(str(res))
