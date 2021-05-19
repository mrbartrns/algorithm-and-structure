"""
스티커 모으기(2)
"""


def solution(sticker):
    if len(sticker) > 2:
        answer = 0
        size = len(sticker) - 1
        dp = [0] * size
        dp[0] = sticker[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
        answer = max(answer, dp[-1])
        sticker.reverse()
        dp = [0] * size
        dp[0] = sticker[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
        answer = max(answer, dp[-1])
        return answer
    else:
        return max(sticker)


sticker = [1, 3, 2, 5, 4]
print(solution(sticker))
