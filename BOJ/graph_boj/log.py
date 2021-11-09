# BOJ 1938 통나무 옮기기
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def can_rotate(cy, cx):
    if cy - 1 < 0 or cy + 1 >= N or cx - 1 < 0 or cx + 1 >= N:
        return False
    for i in range(3):
        for j in range(3):
            if graph[cy - 1 + i][cx - 1 + j] == "1":
                return False
    return True


def rotate(y1, x1, y2, x2, y3, x3):
    ny2, nx2 = y2, x2
    if y2 - 1 == y1 and y2 + 1 == y3 and x1 == x2 == x3:
        ny1, nx1 = y2, x2 - 1
        ny3, nx3 = y2, x2 + 1
    else:
        ny1, nx1 = y2 - 1, x2
        ny3, nx3 = y2 + 1, x2
    return ny1, nx1, ny2, nx2, ny3, nx3


def get_initial_location():
    ret = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "B":
                ret.append(i)
                ret.append(j)
    return ret


def bfs():
    q = []
    visited = set()
    sy1, sx1, sy2, sx2, sy3, sx3 = get_initial_location()
    visited.add((sy1, sx1, sy2, sx2, sy3, sx3))
    heapq.heappush(q, (0, sy1, sx1, sy2, sx2, sy3, sx3))
    while q:
        cnt, y1, x1, y2, x2, y3, x3 = heapq.heappop(q)
        if graph[y1][x1] == "E" and graph[y2][x2] == "E" and graph[y3][x3] == "E":
            return cnt
        for i in range(4):
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]
            ny3 = y3 + dy[i]
            nx3 = x3 + dx[i]
            if (
                ny1 < 0
                or ny1 >= N
                or nx1 < 0
                or nx1 >= N
                or ny2 < 0
                or ny2 >= N
                or nx2 < 0
                or nx2 >= N
                or ny3 < 0
                or ny3 >= N
                or nx3 < 0
                or nx3 >= N
            ):
                continue
            if (
                graph[ny1][nx1] == "1"
                or graph[ny2][nx2] == "1"
                or graph[ny3][nx3] == "1"
            ):
                continue
            if (ny1, nx1, ny2, nx2, ny3, nx3) not in visited:
                visited.add((ny1, nx1, ny2, nx2, ny3, nx3))
                heapq.heappush(q, (cnt + 1, ny1, nx1, ny2, nx2, ny3, nx3))
        if can_rotate(y2, x2):
            ny1, nx1, ny2, nx2, ny3, nx3 = rotate(y1, x1, y2, x2, y3, x3)
            if (ny1, nx1, ny2, nx2, ny3, nx3) not in visited:
                visited.add((ny1, nx1, ny2, nx2, ny3, nx3))
                heapq.heappush(q, (cnt + 1, ny1, nx1, ny2, nx2, ny3, nx3))
    return 0


N = int(si())
graph = [list(si().strip()) for _ in range(N)]
print(bfs())
