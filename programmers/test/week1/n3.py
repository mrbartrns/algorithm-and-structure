"""
조합 방식으로 문제 해결하기
k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
"""
from itertools import combinations
from functools import reduce


def solution(number: str, k: int):
    # 우선 뽑을 숫자들을 조합한다.
    comb = list(combinations(number, len(number) - k))
    # 합친 뒤 숫자로 바꾸어 반환한다.
    arr = list(map(lambda x: int(reduce(lambda acc, cur: acc + cur, x)), comb))
    # 정렬한다.
    arr.sort()
    return str(arr[-1])


number = "4177252841"
k = 4
print(solution(number, k))
