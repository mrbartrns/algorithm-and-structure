"""
최고의 집합
"""


def solution(n, s):
    answer = []
    if s // n == 0:
        answer.append(-1)
        return answer
    for _ in range(n):
        answer.append(s // n)
    share_rest = s % n
    for i in range(share_rest):
        answer[i] += 1
    answer.sort()
    return answer


print(solution(2, 8))
