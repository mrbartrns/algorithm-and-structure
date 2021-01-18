import sys

# 가장 긴 부분수열 알고리즘 이용
def solve(n):
    for i in range(1, n):
        for j in range(i):
            if soldiers[j] < soldiers[i]:
                memo[i] = max(memo[i], memo[j] + 1)
    print(memo)
    return max(memo)


soldiers = [15, 11, 4, 8, 5, 2, 4]
soldiers.reverse()
memo = [1] * len(soldiers)
print(len(soldiers) - solve(len(soldiers)))