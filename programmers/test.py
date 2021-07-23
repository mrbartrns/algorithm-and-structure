# 가장 긴 팰린드롬
def is_palindrome(s, i, j, dp):
    if i >= j:
        return 1

    if dp[i][j] > -1:
        return dp[i][j]

    dp[i][j] = 0
    if s[i] == s[j]:
        dp[i][j] = is_palindrome(s, i + 1, j - 1, dp)
    return dp[i][j]


def solution(s):
    answer = 0
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s, i, j, dp) == 1:
                answer = max(answer, j - i + 1)
    return answer


if __name__ == "__main__":
    a = "abcdcba"
    print(solution(a))