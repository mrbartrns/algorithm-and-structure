import math
from functools import reduce


def solution(n, k):
    ret = list(map(int, filter(lambda x: x, transform(n, k).split("0"))))
    answer = reduce(lambda acc, cur: acc + 1 if is_prime(cur) else acc + 0, ret, 0)
    return answer


def is_prime(n):
    # 빼먹지 말기
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def transform(n, k):
    string = ""
    while n != 0:
        remainder = n % k
        share = n // k
        string = str(remainder) + string
        n = share
    return string


n = 110011
k = 10
print(solution(n, k))
