# 음료수 얼려 먹기
"""
n * m 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어있는것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라
"""
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:  # 나머지 1은 모두 False처리
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True

    return False


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, list(input()))))

print(graph)

res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            res += 1

print(res)
