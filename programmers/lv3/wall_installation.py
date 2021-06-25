# 기둥과 보 설치


def solution(n, build_frame):
    answer = []
    graph = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]
    que = []
    for y, x, a, b in build_frame:
        if b == 1 and condition(y, x, a, graph):
            graph[y][x][a] = True
            que.append((y, x, a))
        elif b == 0:
            graph[y][x][a] = False
            for i in range(n + 1):
                for j in range(n + 1):
                    for k in range(2):
                        if not graph[i][j][k]:
                            continue
                        if not condition(i, j, k, graph):
                            graph[y][x][a] = True
                            break
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(2):
                if graph[i][j][k]:
                    answer.append([i, j, k])
    return answer


def condition(y, x, structure, graph):
    if structure == 0:
        if (
                x == 0
                or (x - 1 >= 0 and graph[y][x - 1][structure])
                or (y - 1 >= 0 and graph[y - 1][x][1 - structure])
                or (graph[y][x][1 - structure])
        ):
            return True
    else:
        if (
                (x - 1 >= 0 and graph[y][x - 1][1 - structure])
                or (y + 1 <= len(graph) and x - 1 >= 0 and graph[y + 1][x - 1][1 - structure])
                or (y - 1 >= 0 and graph[y - 1][x][structure] and y + 1 < len(graph) and graph[y + 1][x][structure])
        ):
            return True
    return False


if __name__ == "__main__":
    n = 5
    # 행, 열, 기둥 또는 보, 설치 또는 삭제
    build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
    print(solution(n, build_frame))
