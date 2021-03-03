# 행렬의 곱셈
def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    l = len(arr1[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(l):
                dp[i][j] += arr1[i][k] * arr2[k][j]
    return dp


arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))