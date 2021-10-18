# BOJ 1976 여행 가자
import sys

# Fluid 안되는 이유 찾기
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def check(parents, plan):
    p = plan[0] - 1
    for i in range(1, M):
        # 이 부분 주의해야 함 -> parents를 direct로 비교하는것이 아닌 get_parent를 통해 두 parent가 일치하는지 확인 필요
        if get_parent(parents, p) != get_parent(parents, plan[i] - 1):
            return False
    return True


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


N = int(si())
M = int(si())
graph = [list(map(int, si().split(" "))) for _ in range(N)]
parents = [i for i in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and get_parent(parents, i) != get_parent(parents, j):
            union_parent(parents, i, j)
plan = list(map(int, si().split(" ")))
print("YES" if check(parents, plan) else "NO")
