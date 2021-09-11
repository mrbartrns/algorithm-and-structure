    """행렬의 테두리만 회전시키는 함수
    가장 왼쪽 위의 좌표를 기준으로 deque 자료구조를 이용하여 삽입한다.
    삽입시에는 열의 모든 값을 넣는것이 아닌, 항상 하나 적은 값까지 한번의 반복문으로 삽입한다.
    4개의 반복문을 이용했을 때 모든 반복문으로 큐에 삽입하는 요소의 갯수가 같아야 한다.
    row + 1, col + 1 만큼 매트릭스를 선언한 후 연산하는것이 편할 수 있다.
    Returns:
        [type]: [description]
    """
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
    """쿼리에 속한 영역을 바탕으로 매트릭스의 값을 추출하는 함수

    Args:
        matrix (list): 2-dimension of list
        query (list): y1, x1, y2, x2 4개의 element로 이루어져 있는 함수

    Returns:
        deque: deque of elements of matrix
    """
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
