import math


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        sqrt = math.sqrt(i)
        answer += i if sqrt - int(sqrt) > 0 else -i
    return answer


left = 24
right = 27
print(solution(left, right))
