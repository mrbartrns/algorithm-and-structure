"""
2. 군인 정렬하기
N명의 전사가 무작위로 배열되어 있다. 이때, 병사들은 특정한 값의 전투력을 가질때, 전투력이 높은순서부터 낮은 순서대로 배열을 하고자 한다.
최소한으로 병사를 제외하여 내림차순을 만들 수 있을때, 제외해야 할 병사의 수는?
"""


def solve(n):
    for i in range(1, n):
        for j in range(i):
            if soldiers[i] > soldiers[j]:
                memo[i] = max(memo[i], memo[j] + 1)
    return max(memo)


soldiers = [15, 11, 4, 8, 5, 2, 4]
soldiers.reverse()
memo = [1] * len(soldiers)  # 어떠한 요소들간의 관계가 없다면, 각 부분수열의 길이는 모두 1이다.
print(len(soldiers) - solve(len(soldiers)))  # 2
