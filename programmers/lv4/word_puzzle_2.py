INF = 987654321


def solution(strs, t):
    dp = [INF] * (len(t) + 1)
    dp[0] = 0

    for i in range(1, len(t) + 1):
        for j in range(1, 6):
            if i - j < 0:
                continue
            s = i - j
            if t[s: i] in strs:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[len(t)] if dp[len(t)] < INF else -1


if __name__ == '__main__':
    strs = ["ba", "na", "n", "a"]
    t = "banana"
    print(solution(strs, t))
