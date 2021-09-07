# 짝수 행 세기
MOD = 10000019


def solution(a):
    row, col = len(a), len(a[0])
    arr_one_cnt = calculate_one_count(a)
    ncr = [[0 for _ in range(row + 1)] for _ in range(row + 1)]
    get_binomial_coefficient(row, ncr)
    # dp[a][b] = c 1열부터 a열까지 계산 했을 때 b개의 짝수행을 가진 배열은 총 c가지가 있다
    dp = [[0 for _ in range(row + 1)] for _ in range(col + 2)]
    dp[1][row - arr_one_cnt[0]] = ncr[row][row - arr_one_cnt[0]]

    for column in range(1, col):
        one_cnt = arr_one_cnt[column]
        for even_num in range(row + 1):
            if dp[column][even_num] == 0:
                continue
            for k in range(one_cnt + 1):
                if even_num < k:
                    continue
                be_even_row = even_num + one_cnt - (2 * k)
                if be_even_row > row:
                    continue
                result = (ncr[even_num][k] * ncr[row - even_num][one_cnt - k]) % MOD
                dp[column + 1][be_even_row] = (
                    dp[column + 1][be_even_row] + dp[column][even_num] * result
                )
                dp[column + 1][be_even_row] %= MOD
    return dp[col][row]


def calculate_one_count(a):
    ret = [0] * (len(a[0]) + 1)
    for i in range(len(a)):
        for j in range(len(a[0])):
            ret[j] += a[i][j]
    return ret


# 행 만큼의 경우의 수를 만든다.
def get_binomial_coefficient(n, dp):
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(n + 1):
            if j == 0:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

            dp[i][j] %= MOD


def get_binomial_coefficient_recursive(n, r, dp):
    if dp[n][r] > -1:
        return dp[n][r]

    if r == 0 or n == r:
        dp[n][r] = 1
        return dp[n][r]

    # 이항계수의 정의에 의하여
    dp[n][r] = get_binomial_coefficient(n - 1, r - 1, dp) + get_binomial_coefficient(
        n - 1, r, dp
    )
    return dp[n][r]


if __name__ == "__main__":
    a = [[1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1]]
    print(solution(a))
