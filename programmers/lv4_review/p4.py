# 단어 퍼즐
INF = 987654321


def solution(strs, t):
    dp = [INF] * (len(t) + 1)
    dp[0] = 0
    for i in range(1, len(dp)):
        for j in range(1, 6):
            idx = i - j if i - j > 0 else 0
            if t[idx:i] in strs:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[len(t)] if dp[len(t)] < INF else -1


if __name__ == '__main__':
    strs = ["ba", "na", "n", "a"]
    t = "banana"
    print(solution(strs, t))
