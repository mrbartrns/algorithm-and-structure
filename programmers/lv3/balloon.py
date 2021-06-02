# 풍선 터트리기
def solution(a):
    answer = 0
    dp = [0] * 1000001
    dp2 = [0] * 1000001
    dp[0] = a[0]
    for i in range(1, len(a)):
        if dp[i - 1] > a[i]:
            dp[i] = a[i]
        else:
            dp[i] = dp[i - 1]
    dp2[len(a) - 1] = a[len(a) - 1]
    for i in range(len(a) - 2, -1, -1):
        if dp2[i + 1] > a[i]:
            dp2[i] = a[i]
        else:
            dp2[i] = dp2[i + 1]
    for i in range(len(a)):
        if a[i] <= dp[i] or a[i] <= dp2[i]:
            answer += 1
    return answer
