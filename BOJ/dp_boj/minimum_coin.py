# 동전의 종류
coins = [1, 5, 11]

# 거슬러줘야 할 금액
n = 15

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = -1
    for coin in coins:
        if coin <= i:
            if dp[i - coin] < 0:
                continue
            if dp[i] < 0:
                dp[i] = dp[i - coin] + 1
            elif dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

print(dp)