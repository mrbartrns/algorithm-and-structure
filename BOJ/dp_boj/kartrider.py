# BOJ 17391 무한 부스터
"""
모든 격자 안에는 특정 개수의 부스터 아이템이 위치
카트 바디가 격자에 멈춰 있을 때, 격자에 놓여있는 부스터 아이템을 자동으로 전부 습득
x개를 습득했다면 오른쪽으로 최대 X 칸을 가거나 아래쪽으로 최대 X칸을 이동할 수 있음
이동 후 멈추면서 보유하고 있던 부스터 아이템은 모두 소진
"""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

N, M = map(int, si().split(" "))  # 행, 열
booster = [list(map(int, si().split(" "))) for _ in range(N)]
cache = [[-1 for _ in range(M)] for _ in range(N)]


def move(y, x):
    if y >= N or x >= M:
        return INF

    if y == N - 1 and x == M - 1:
        return 0

    if cache[y][x] > -1:
        return cache[y][x]

    cache[y][x] = INF
    count = booster[y][x]
    for i in range(1, count + 1):
        cache[y][x] = min(cache[y][x], move(y + i, x) + 1)
        cache[y][x] = min(cache[y][x], move(y, x + i) + 1)
    return cache[y][x]


print(move(0, 0))
