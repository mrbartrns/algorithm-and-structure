# 카드 짝 맞추기
import copy
from collections import deque
from itertools import permutations

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def solution(board, r, c):
    answer = INF
    cards = find_card(board)
    orders = list(permutations(cards))
    cards_idx = get_card_idx(board)
    same_card_orders = []
    get_order(same_card_orders, len(cards), [], 0)
    locations = setting(cards_idx, orders, same_card_orders)
    for i in range(len(locations)):
        for j in range(len(locations[i])):
            res = 0
            copied_board = copy.deepcopy(board)
            cur_y, cur_x = r, c
            for k in range(len(locations[i][j])):
                sy, sx = locations[i][j][k]
                res += bfs(copied_board, cur_y, cur_x, sy, sx)
                cur_y, cur_x = sy, sx
            answer = min(answer, res)

    return answer


def find_card(board):
    existed = [False for _ in range(len(board) * len(board) + 1)]
    ret = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                continue
            card = board[i][j]
            if not existed[card]:
                existed[card] = True
                ret.append(card)
    return ret


def get_card_idx(board):
    ret = [[] for _ in range(len(board) * len(board) + 1)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                continue
            card = board[i][j]
            ret[card].append([i, j])
    return ret


def get_order(orders, length, cur, cnt):
    if cnt == length:
        orders.append(cur[:])
        return
    for i in range(2):
        cur.append(i)
        get_order(orders, length, cur, cnt + 1)
        cur.pop()


def setting(cards_idx, orders, same_card_orders):
    ret = []
    for i in range(len(orders)):
        order = orders[i]
        temp = []
        for j in range(len(same_card_orders)):
            temp1 = []
            for k in range(len(same_card_orders[j])):
                idx = order[k]
                same_card_idx = same_card_orders[j][k]
                temp1.append(cards_idx[idx][same_card_idx])
                temp1.append(cards_idx[idx][1 - same_card_idx])
            temp.append(temp1)
        ret.append(temp)
    return ret


def bfs(maps, sy, sx, ey, ex):
    que = deque()
    visited = [[False for _ in range(len(maps))] for _ in range(len(maps))]
    que.append((sy, sx, 0))
    while que:
        y, x, cnt = que.popleft()
        if y == ey and x == ex:
            maps[ey][ex] = 0
            return cnt + 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(maps) or nx < 0 or nx >= len(maps):
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            while True:
                if ny < 0 or ny >= len(maps) or nx < 0 or nx >= len(maps):
                    ny -= dy[i]
                    nx -= dx[i]
                    break
                if maps[ny][nx] > 0:
                    break
                ny += dy[i]
                nx += dx[i]

            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))


if __name__ == "__main__":
    board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
    print(solution(board, 0, 1))
