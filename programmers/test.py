def solution(n, k):
    dp = [0] * 21
    dp[0] = 1
    for i in range(1, 21):
        dp[i] = dp[i - 1] * i
    arr = [i + 1 for i in range(n)]
    return solve(n, k - 1, dp, set(), arr)


def solve(n, k, dp, s, arr):
    answer = []
    if n < 0:
        return answer
    idx = k // dp[n - 1]
    left = k % dp[n - 1]
    cnt = 0
    for i in range(len(arr)):
        if arr[i] not in s:
            if cnt == idx:
                s.add(arr[i])
                answer.append(arr[i])
                break
            cnt += 1
    answer += solve(n - 1, left, dp, s, arr)
    return answer


if __name__ == "__main__":
    n = 3
    k = 5
    print(solution(n, k))