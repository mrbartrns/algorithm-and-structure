# 가장 긴 팰린드롬의 길이
import sys

sys.setrecursionlimit(2501)


def solution(s):
    answer = 0
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            if is_palindrome(i, j, s, dp):
                answer = max(answer, j - i + 1)
    return answer


def is_palindrome(i, j, s, dp):
    if i >= j:
        return 1

    if s[i] != s[j]:
        dp[i][j] = 0
        return dp[i][j]

    if dp[i][j] > -1:
        return dp[i][j]

    dp[i][j] = is_palindrome(i + 1, j - 1, s, dp)
    return dp[i][j]


if __name__ == "__main__":
    s = "abacde"
    print(solution(s))
