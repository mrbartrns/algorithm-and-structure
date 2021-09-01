# 짝수 행 세기

def solution(a):
    row, col = len(a), len(a[0])
    arr_one_cnt = []
    for j in range(col):
        cnt = 0
        for i in range(row):
            cnt += a[i][j]
        arr_one_cnt.append(cnt)
    print(arr_one_cnt)
    # dp[a][b] = c 1열부터 a열까지 계산 했을 때 b개의 짝수행을 가진 배열은 총 c가지가 있다


# 행 만큼의 경우의 수를 만든다.
def get_binomial_coefficient(n, r, dp):
    if dp[n][r] > -1:
        return dp[n][r]

    if n == r or r == 0:
        dp[n][r] = 1
        return dp[n][r]

    dp[n][r] = get_binomial_coefficient(n - 1, r, dp) + get_binomial_coefficient(n - 1, r - 1, dp)
    return dp[n][r]


if __name__ == '__main__':
    a = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]]
    # dp = [[-1 for _ in range(len(a) + 1)] for _ in range(len(a) + 1)]
    # for i in range(1, len(a) + 1):
    #     for j in range(i + 1):
    #         get_binomial_coefficient(i, j, dp)
    # print(dp)
    print(solution(a))
