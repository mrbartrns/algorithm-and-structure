# 스티커 모으기2
def solution(sticker):
    if len(sticker) > 1:
        size = len(sticker)
        dp = [0] * (size - 1)
        dp[0] = sticker[0]
        for i in range(1, size - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
        answer = dp[-1]
        dp = [0] * (size - 1)
        sticker.reverse()
        dp[0] = sticker[0]
        for i in range(1, size - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
        answer = max(answer, dp[-1])
        return answer
    else:
        return sticker[0]


if __name__ == "__main__":
    sticker = [14]
    print(solution(sticker))
