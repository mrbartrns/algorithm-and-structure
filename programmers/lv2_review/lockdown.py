    """2차원 다익스트라의 경우 오류가 나기때문에 경로가 있는 deque 자료구조를 사용하면 오류가 없다.
    """
# [카카오] 거리두기 확인하기
from collections import deque

INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra(y, x, place):
    distance = [[INF for _ in range(5)] for _ in range(5)]
    distance[y][x] = 0
    que = deque()
    que.append((y, x, 0))
    while que:
        y, x, cost = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue

            if place[ny][nx] == "X":
                continue

            if cost + 1 < distance[ny][nx]:
                distance[ny][nx] = cost + 1
                que.append((ny, nx, cost + 1))
    return distance


def check(place):
    people = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                people.append((i, j))
    for y, x in people:
        distance = dijkstra(y, x, place)
        for p, q in people:
            if y == p and x == q:
                continue
            if distance[p][q] <= 2:
                return False
    return True


def solution(places):
    answer = []
    for place in places:
        answer.append(1 if check(place) else 0)
    return answer


if __name__ == "__main__":
    places = [
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ]

    print(solution(places))