# 짝수 행 세기
# TODO: read and understand again
MOD = 10000019


def get_one_cnt(a):
    ret = [0] * len(a[0])
    for i in range(len(a)):
        for j in range(len(a[0])):
            ret[j] += a[i][j]
    return ret


def get_binomial_coefficient(n, dp):
    """행의 갯수에 따른 경우의 수를 구하는 함수"""
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(n + 1):
            if j == 0:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD


#
def solution(a):
    row, col = len(a), len(a[0])
    # 열이 기준이 된다.
    arr_one_cnt = get_one_cnt(a)
    ncr = [[0 for _ in range(row + 1)] for _ in range(row + 1)]
    get_binomial_coefficient(row, ncr)
    dp = [[0 for _ in range(row + 1)] for _ in range(col + 2)]
    # 첫번째 열에 대하여 먼저 계산
    dp[1][row - arr_one_cnt[0]] = ncr[row][row - arr_one_cnt[0]]
    # 나머지 열에 대하여 계산
    for i in range(1, col):
        one_cnt = arr_one_cnt[i]
        for j in range(row + 1):
            if dp[i][j] == 0:
                continue
            for k in range(one_cnt + 1):
                if j < k:
                    continue
                nxt_even_row_cnt = j + one_cnt - (2 * k)
                if nxt_even_row_cnt > row:
                    continue
                result = ncr[j][k]


if __name__ == "__main__":
    a = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(solution(a))