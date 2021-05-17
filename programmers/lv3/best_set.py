"""
최고의 집합
"""


def solution(n, s):
    answer = []
    a = s // n
    b = s - a
    if a == 0 or b == 0:
        answer.append(-1)
    else:
        answer.append(a)
        answer.append(b)
        answer.sort()
    return answer


print(solution(2, 9))
