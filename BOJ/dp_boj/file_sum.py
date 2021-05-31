# BOJ 11066
import sys

si = sys.stdin.readline
INF = 1e9

t = int(si())
for _ in range(t):
    # 챕터의 갯수 및 챕터의 크기를 배열로 만들기
    k = int(si())
    cost = [0] + list(map(int, si().split()))

    # 만들수 있는 최대 배열의 크기로 dp 배열 만들기
    dp = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
    psum = [0] * 501

    for i in range(1, k + 1):
        # 부분합을 만들어 저장하기
        psum[i] = psum[i - 1] + cost[i]

    # d가 하는 역할은? 동일한 배열을 이용하므로 중복되는 계산을 방지하기 위한 배열
    for d in range(1, k):
        for tx in range(1, k + 1):
            ty = tx + d

            if ty <= k:
                dp[tx][ty] = INF
                for mid in range(tx, ty):
                    dp[tx][ty] = min(
                        dp[tx][ty],
                        dp[tx][mid] + dp[mid + 1][ty] + psum[ty] - psum[tx - 1],
                    )
            else:
                break

    print(dp[1][k])