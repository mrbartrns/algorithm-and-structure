# 카드 짝 맞추기
from collections import deque


def solution(board, r, c):
    answer = 0
    return answer


def bfs(board, r, c):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    que = deque()
    to_str = to_string(board)
    visited = set()
    if board[r][c] > 0:
        que.append((r, c, to_str, 1, r, c))
    que.append((r, c, to_str, 0, -1, -1))
    while que:
        y, x, to_str, cnt, prev_y, prev_x = que.popleft()
        print(y, x)

        if to_str == "0000000000000000":
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            graph = to_graph(to_str)
            if ny < 0 or ny >= 2 or nx < 0 or nx >= 2:
                continue

            if graph[ny][nx] > 0:
                if prev_y > -1 and prev_x > -1 and graph[prev_y][prev_x] == graph[ny][nx]:
                    graph[ny][nx] = 0
                    graph[prev_y][prev_x] = 0
                    new_str = to_string(graph)
                    que.append((ny, nx, new_str, cnt + 2, -1, -1))
                elif prev_y > -1 and prev_x > -1 and graph[prev_y][prev_x] != graph[ny][nx]:
                    que.append((ny, nx, to_str, cnt + 1, prev_y, prev_x))
                else:
                    que.append((ny, nx, to_str, cnt + 1, prev_y, prev_x))
                    que.append((ny, nx, to_str, cnt + 2, ny, nx))
            else:
                que.append((ny, nx, to_str, cnt + 1, prev_y, prev_x))

            # graph = to_graph(to_str)
            # while 0 < ny < 3 and 0 < nx < 3:
            #     ny += dy[i]
            #     nx += dx[i]
            #     if graph[ny][nx] > 0:
            #         break
            #
            # if graph[ny][nx] > 0:
            #     if prev_y > 0 and prev_x > 0 and graph[prev_y][prev_x] == graph[ny][nx]:
            #         graph[ny][nx] = 0
            #         graph[prev_y][prev_x] = 0
            #         new_str = to_string(graph)
            #         que.append((ny, nx, new_str, cnt + 2, -1, -1))
            #     elif prev_y > 0 and prev_x > 0 and graph[prev_y][prev_x] != graph[ny][nx]:
            #         que.append((ny, nx, to_str, cnt + 1, prev_y, prev_x))
            #     else:
            #         que.append((ny, nx, to_str, cnt + 1, prev_y, prev_x))
            #         que.append((ny, nx, to_str, cnt + 2, ny, nx))
            # else:
            #     que.append((ny, nx, to_str, cnt + 1, prev_y, prev_x))


def to_graph(string):
    graph = []
    for i in range(2):
        temp = []
        for j in range(2):
            temp.append(int(string[2 * i + j]))
        graph.append(temp)
    return graph


def to_string(graph):
    string = ""
    for i in range(2):
        for j in range(2):
            string += str(graph[i][j])
    return string


if __name__ == "__main__":
    board = [[1, 1], [2, 2]]
    r, c = 0, 0
    print(bfs(board, r, c))
