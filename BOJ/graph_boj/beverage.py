# 음료수 얼려먹기
"""
n * m의 얼음 틀에서 구멍이 뚤려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
얼음 틀이 주어졌을 때, 만들수 있는 아이스크림의 갯수를 구하시오
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 재귀함수의 기저 조건 > 항상 먼저 써두어 헷갈리지 않게 하기
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True  # 재귀함수의 리턴값과 상관 없이 무조건 첫 진입시 조건이 성립한다면 True 처리. 조건 처리시 유용함
        # 모든 재귀함수가 변하는 분할정복 형식의 리턴값을 가져야 하는것은 아니다.

    # 이미 1로 처리된 것들에 대해서 더 탐색하지 않음
    return False


res = 0
# 현재 dfs함수가 정해진 위치에서 탐색하도록 되있으므로, 그래프를 모두 순회해야 한다.
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            res += 1

print(res)