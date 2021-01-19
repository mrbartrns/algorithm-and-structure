"""
개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다. 메뚜기 마을에는 여러개의 식량창고가 이어져 있는데 모두 일직선이다. (리스트)
각 식량창고는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 뺏을 예정이다. 
개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
"""

stores = [1, 3, 1, 5]
# 1번 창고를 털때는 1번만 가져올 수 있다.
memo = [0] * len(stores)
memo[0] = stores[0]
memo[1] = max(stores[0], stores[1])


def solve(n):
    if n < 2:
        return memo[n]

    if memo[n] > 0:
        return memo[n]

    memo[n] = max(solve(n - 1), solve(n - 2) + stores[n])  # 조각들의 부분 해를 합하여 전체해를 구성. 점화식
    return memo[n]
