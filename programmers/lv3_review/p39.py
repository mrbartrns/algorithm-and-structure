# 줄 서는 방법
def solution(n, k):
    dp = [0] * 21
    dp[0] = 1
    for i in range(1, 21):
        dp[i] = i * dp[i - 1]
    s = set()
    arr = [i for i in range(1, n + 1)]
    answer = get_arr(n, k - 1, dp, s, arr)
    return answer


def get_arr(n, k, dp, s, arr):
    answer = []
    if n < 0:
        return answer
    idx = k // dp[n - 1]
    left = k % dp[n - 1]
    cnt = 0
    chk = 0
    while cnt < len(arr):
        if arr[cnt] not in s:
            if chk == idx:
                s.add(arr[cnt])
                answer = [arr[cnt]] + get_arr(n - 1, left, dp, s, arr)
                break
            chk += 1
        cnt += 1

    return answer


if __name__ == "__main__":
    n = 3
    k = 6
    print(solution(n, k))
