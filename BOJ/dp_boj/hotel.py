# BOJ 1106 호텔
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

INF = 987654321
answer = INF
C, N = map(int, si().split(" "))
dp = [INF] * 1500
dp[0] = 0
arr = []
for _ in range(N):
    arr.append(list(map(int, si().split(" "))))  # 비용, 고객수
for cost, customer in arr:
    for cur_customer in range(customer, C + 101):
        dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)
for i in range(C, C + 101):
    answer = min(dp[i], answer)
print(answer)