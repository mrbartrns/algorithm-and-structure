# 행렬 회전하기
from collections import deque


def display(que, matrix, query):
    y1, x1, y2, x2 = query
    idx = 0
    for j in range(x1, x2):
        matrix[y1][j] = que[idx]
        idx += 1
    for i in range(y1, y2):
        matrix[i][x2] = que[idx]
        idx += 1
    for j in range(x2, x1, -1):
        matrix[y2][j] = que[idx]
        idx += 1
    for i in range(y2, y1, -1):
        matrix[i][x1] = que[idx]
        idx += 1


def get_target(matrix, query):
    y1, x1, y2, x2 = query
    que = deque()
    for j in range(x1, x2):
        que.append(matrix[y1][j])
    for i in range(y1, y2):
        que.append(matrix[i][x2])
    for j in range(x2, x1, -1):
        que.append(matrix[y2][j])
    for i in range(y2, y1, -1):
        que.append((matrix[i][x1]))
    return que


def make_matrix(rows, cols):
    matrix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    cnt = 1
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            matrix[i][j] = cnt
            cnt += 1
    return matrix


def solution(rows, columns, queries):
    answer = []
    matrix = make_matrix(rows, columns)
    for query in queries:
        que = get_target(matrix, query)
        que.rotate(1)
        answer.append(min(que))
        display(que, matrix, query)

        # for i in range(1, rows + 1):
        #     for j in range(1, columns + 1):
        #         print(matrix[i][j], end=" ")
        #     print()
        # print()
    return answer


if __name__ == "__main__":
    rows = 100
    columns = 97
    queries = [[1, 1, 100, 97]]
    print(solution(rows, columns, queries))
