"""
개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다. 메뚜기 마을에는 여러개의 식량창고가 이어져 있는데 모두 일직선이다. (리스트)
각 식량창고는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 뺏을 예정이다. 
개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
"""

# 구하는것은 창고를 털었을 때 얻을 수 있는 최대 식량의 양이므로, 메모할 것은 각 창고를 순서대로 털었을 때 얻을 수 있는 최대 식량의 수이다.
# 어떤 위치에서 창고를 털 때 얻을 수 있는 식량은, 인접한 식량창고 의 식량합과 그 이전 창고에서의 식량합과 그 위치에서의 식량을 더했을때 둘중 더 큰값이 된다
# 점화식: ak = max(ak-2 + ak, ak-1)
# 이전의 누적 합을 이용하므로 다이나믹 프로그래밍의 조건에 성립한다.

# 재귀로 짰을 때 (탑다운 방식)
def solve(idx: int):
    # 0번 인덱스와 1번인덱스에서 얻을수 있는 최대 식량의 수는 각각 같다. 0번 인덱스를 선택하면 1번 인덱스의 값을 얻을 수 없고, 그 반대도 마찬가지이기 때문이다. (비교 대상 자체가 없다)
    if idx < 2:
        return store[idx]

    if memo[idx] > 0:
        return memo[idx]

    memo[idx] = max(solve(idx - 1), solve(idx - 2) + store[idx])
    return memo[idx]


# 반복문으로 짰을 때 (바텀업 방식)
def solve_iter(idx: int):
    memo[0], memo[1] = store[0], store[1]
    for i in range(2, len(store)):
        memo[i] = max(memo[i - 1], memo[i - 2] + store[i])
    return memo[idx]


store = [1, 3, 1, 5]
memo = [0] * len(store)
print(solve(3))
print(solve_iter(3))