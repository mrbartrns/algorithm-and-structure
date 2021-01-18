"""
개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다. 메뚜기 마을에는 여러개의 식량창고가 이어져 있는데 모두 일직선이다. (리스트)
각 식량창고는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 뺏을 예정이다. 
개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
"""

store = [1, 3, 1, 5]
has_visited = [False] * len(store)
values = []

"""
def solve(idx, tot):
    # 더 이상 탐색할 수 없을때 종료 > 어느 조건에서 탐색할 수 없는지?
    if idx >= len(store) - 2:
        values.append(tot)
        return

    for i in range(len(store)):
        if not has_visited[i] and i >= idx:
            if i == 0 or not has_visited[i - 1]:
                has_visited[i] = True
                idx = i
                solve(idx, tot + store[i])
                has_visited[i] = False


"""
# dp로 풀었을 때 백트래킹을 이용하지 않고도 리턴값을 갖게 하는 재귀함수 구성이 가능
memo = [0] * len(store)


def solve(idx):  # idx는 창고 번호
    if idx < 2:
        return store[idx]

    if memo[idx] > 0:
        return memo[idx]

    memo[idx] = max(solve(idx - 1), solve(idx - 2) + store[idx])
    return memo[idx]


for i in range(len(store)):
    print(solve(i))