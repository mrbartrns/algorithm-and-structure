# [카카오] 거리두기 확인하기
from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def check(place):
    locations = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                locations.append((i, j))
    for p, q in locations:
        distance = dijkstra(p, q, place)
        for y in range(5):
            for x in range(5):
                if y == p and x == q:
                    continue
                if place[y][x] == "P" and distance[y][x] <= 2:
                    return False
    return True


def dijkstra(y, x, place):
    que = deque()
    distance = [[INF for _ in range(5)] for _ in range(5)]
    distance[y][x] = 0
    que.append((y, x, 0))
    while que:
        y, x, dist = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            if place[ny][nx] == "X":
                continue
            if distance[ny][nx] > dist + 1:
                distance[ny][nx] = dist + 1
                que.append((ny, nx, dist + 1))
    return distance


def solution(places):
    answer = []
    for place in places:
        ret = check(place)
        answer.append(1 if ret else 0)
    return answer


if __name__ == "__main__":
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
    print(solution(places))