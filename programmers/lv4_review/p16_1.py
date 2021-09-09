# 짝수 행 세기
# TODO: read and understand again


MOD = 10000019


def get_binomial_coefficient(dp):
    dp[0][0] = 1
    for i in range(1, len(dp)):
        for j in range(len(dp)):
            if j == 0:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]


def get_one_cnt(a):
    ret = [0] * len(a[0])
    for i in range(len(a)):
        for j in range(len(a[0])):
            ret[j] += a[i][j]
    return ret


def solution(a):
    row = len(a)
    col = len(a[0])
    arr_one_cnt = get_one_cnt(a)
    ncr = [[0 for _ in range(row + 1)] for _ in range(row + 1)]
    get_binomial_coefficient(ncr)
    dp = [[0 for _ in range(row + 1)] for _ in range(col + 2)]
    # calculate dp[0]
    dp[1][row - arr_one_cnt[0]] = ncr[row][row - arr_one_cnt[0]]

    for i in range(1, col):
        one_cnt = arr_one_cnt[i]
        for even_row in range(row + 1):
            if dp[i][even_row] == 0:
                continue
            # k는 기존 짝수행에 추가할 1의 갯수
            for k in range(one_cnt + 1):
                if k > even_row:
                    continue
                be_even_row = even_row + one_cnt - 2 * k
                if be_even_row > row:
                    continue
                result = (ncr[even_row][k] * ncr[row - even_row][one_cnt - k]) % MOD
                dp[i + 1][be_even_row] = (
                    result * dp[i][even_row] + dp[i + 1][be_even_row]
                ) % MOD
    return dp[col][row]


if __name__ == "__main__":
    a = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(solution(a))