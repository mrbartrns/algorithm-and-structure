# BOJ 12100
import sys
import copy

si = sys.stdin.readline


def move(maps, direction):
    """
    1. 이동하기 전 direction방향으로 모두 당기기
    2. 인접한 숫자가 같은지 확인 후 같다면 한번만 direction방향으로 합치기
    3. 다시 숫자를 당기기
    @param maps: list
    @param direction: int
    @return: None
    """
    if direction == 0:  # 북쪽
        for j in range(n):
            for i in range(n):
                if maps[i][j] == 0:
                    for k in range(i + 1, n):
                        if maps[k][j] > 0:
                            maps[i][j], maps[k][j] = maps[k][j], maps[i][j]
                            break
    elif direction == 1:  # 동쪽
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if maps[i][j] == 0:
                    for k in range(j - 1, -1, -1):
                        if maps[i][k] > 0:
                            maps[i][j], maps[i][k] = maps[i][k], maps[i][j]
                            break
    elif direction == 2:  # 남쪽
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if maps[i][j] == 0:
                    for k in range(i - 1, -1, -1):
                        if maps[k][j] > 0:
                            maps[i][j], maps[k][j] = maps[k][j], maps[i][j]
                            break
    elif direction == 3:  # 서쪽
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 0:
                    for k in range(j + 1, n):
                        if maps[i][k] > 0:
                            maps[i][j], maps[i][k] = maps[i][k], maps[i][j]
                            break


def check(maps, direction):
    """
    1.
    @param maps: list
    @param direction: int
    @return: None
    """
    if direction == 0:  # 북쪽
        for j in range(n):
            for i in range(n):
                if i + 1 < n and maps[i][j] == maps[i + 1][j]:
                    maps[i][j] += maps[i + 1][j]
                    maps[i + 1][j] = 0
    elif direction == 1:  # 동쪽
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if j - 1 >= 0 and maps[i][j] == maps[i][j - 1]:
                    maps[i][j] += maps[i][j - 1]
                    maps[i][j - 1] = 0
    elif direction == 2:  # 남쪽
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if i - 1 >= 0 and maps[i][j] == maps[i - 1][j]:
                    maps[i][j] += maps[i - 1][j]
                    maps[i - 1][j] = 0
    elif direction == 3:  # 서쪽
        for i in range(n):
            for j in range(n):
                if j + 1 < n and maps[i][j] == maps[i][j + 1]:
                    maps[i][j] += maps[i][j + 1]
                    maps[i][j + 1] = 0


def backtrack(maps, k):
    """
    1. string map을 입력받아 백트래킹시 현재 상태의 저장이 필요
    @param maps: list
    @param k: int
    @return: None
    """
    if k == 5:
        max_value = 0
        for i in range(n):
            for j in range(n):
                if max_value < maps[i][j]:
                    max_value = maps[i][j]
        res.add(max_value)
        return
    for d in range(4):
        # 그래프 복사
        copied_maps = copy.deepcopy(maps)
        move(copied_maps, d)
        check(copied_maps, d)
        move(copied_maps, d)
        backtrack(copied_maps, k + 1)


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]

res = set()
backtrack(graph, 0)
print(max(res))
