# 주어진 n가지의 동전으로 최소의 동전 수를 이용하여 금액을 맞추기
# 주어진 동전을 외부 for문, 내부 for문을 금액순회로 두는것이 키포인트이다. 그러면 이중 삼중으로 확인할 필요가 없다.
# 현재 금액의 최소값을 확인하기 위해서 동전을 뺀 만큼에서의 동전 최솟값에 1을 더한값이 최소가 된다. 즉 동적 계획법을 이용할 수 있다.
# limit을 문제범위보다 큰 값을 사용하여 줄여나가는 형식으로 작성한다.
import sys

input = sys.stdin.readline

# coins = [2, 3]


def solve(n, m):
    for i in range(n):
        for j in range(m):  # 작은 금액부터 순회하므로 다이나믹 프로그래밍의 조건을 만족.
            if memo[j - coins[i]] != LIMIT:
                memo[j] = min(memo[j], memo[j - coins[i]] + 1)
    return memo[m] if memo[m] != 10001 else -1


n, m = map(int, input().split())
LIMIT = 10001
memo = [LIMIT] * (m + 1)  # 동전의 최대 갯수, m은 금액
memo[0] = 0
coins = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)