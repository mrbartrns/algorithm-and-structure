# 단어 퍼즐

INF = 987654321


def solution(strs, t):
    dp = [INF] * (len(t) + 1)
    dp[0] = 0
    for i in range(1 + len(t)):
        for j in range(1, 6):
            s = i - j
            # 단어를 복사할 때 i 인덱스의 글자는 포함하지 않으므로
            # [0:1]은 0번 인덱스만 존재하기 때문에 dp 배열을 단어의 길이보다 1 높게 설정하여 1부터 탐색하는것이 나을 수 있다.
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[len(t)] if dp[len(t)] < INF else -1


if __name__ == '__main__':
    strs = ["ba", "na", "n", "a"]
    t = "banana"
    print(solution(strs, t))
