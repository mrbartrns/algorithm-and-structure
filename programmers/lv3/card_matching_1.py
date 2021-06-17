# 카드 짝 맞추기
"""
1. 현재 보드를 모두 순회하면서 카드의 종류를 모두 긁어 모은다.
2. 순회한 보드에 따라 permutations 한다.
3. 방문할 좌표들을 백트래킹한다. -> 좌표들을 저장하고 좌표의 인덱스만 백트래킹한다.
4. 방문해야할 모든 좌표 세트를 구하고 bfs를 실행한다.
"""
import copy
from collections import deque
from itertools import permutations

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def get_card(board):
    ret = []
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0 and board[i][j] not in ret:
                ret.append(board[i][j])
    return ret


def get_card_idx(board):
    ret = [[] for _ in range(10)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] > 0:
                cur_card = board[i][j]
                ret[cur_card].append((i, j))
    return ret


def backtrack(idx, cur_order, vector, arr, card_idx):
    if idx == len(cur_order):
        vector.append(arr[:])
        return
    for i in range(2):
        cur_number = cur_order[idx]
        arr.append(card_idx[cur_number][i])
        arr.append(card_idx[cur_number][1 - i])
        backtrack(idx + 1, cur_order, vector, arr, card_idx)
        arr.pop()
        arr.pop()


def solution(board, r, c):
    n = len(board)
    ans = INF
    card = []
    card_idx = [[] for _ in range(10)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                if board[i][j] not in card:
                    card.append(board[i][j])
                card_idx[board[i][j]].append((i, j))
    card_list = list(permutations(card))
    visit_order = []
    for cur_order in card_list:
        backtrack(0, cur_order, visit_order, [], card_idx)

    for vector in visit_order:
        graph = copy.deepcopy(board)
        cur_y, cur_x = r, c
        res = 0
        for y, x in vector:
            res += bfs(graph, cur_y, cur_x, y, x)
            cur_y, cur_x = y, x
        ans = min(ans, res)
    return ans


def bfs(board, sy, sx, ey, ex):
    n = len(board)
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[sy][sx] = True
    que.append((sy, sx, 0))
    while que:
        y, x, cnt = que.popleft()
        if y == ey and x == ex:
            board[y][x] = 0
            return cnt + 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            while True:
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    ny -= dy[i]
                    nx -= dx[i]
                    break

                if board[ny][nx] > 0:
                    break

                ny += dy[i]
                nx += dx[i]

            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))


if __name__ == "__main__":
    board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
    print(solution(board, 0, 1))
