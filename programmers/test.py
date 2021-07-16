def solution(sticker):
    if len(sticker) <= 1:
        return sticker[0]
    dp = [0] * 100001
    dp[0] = sticker[0]
    for i in range(1, len(sticker) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    answer = dp[len(sticker) - 2]
    dp = [0] * 100001
    sticker.reverse()
    dp[0] = sticker[0]
    for i in range(1, len(sticker) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    answer = max(answer, dp[len(sticker) - 2])
    return answer


if __name__ == "__main__":
    sticker = [14, 6, 5, 11, 3, 9, 2, 10]
    print(solution(sticker))
