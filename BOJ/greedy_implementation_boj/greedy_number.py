# 그리디 대표유형
# 그리디는 항상 그 방법의 정당성의 분석이 중요
"""
이 경우에는 그리디 사용 가능 > 어떤 한 수만으로 계속 나눌 때, 나누는 것은 1을 빼는 것 보다 경우의수가 항상 작거나 같기 때문
"""
n, k = map(int, input().split())


def solve(n, k):
    res = 0
    num = n
    while num > 1:
        if n % k != 0:
            num -= 1
        else:
            num //= k
        res += 1
    return res


# 좀 더 테크닉적인 방법
def s(n, k):
    result = 0
    while True:
        target = (n // k) * k  # 나눈 수
        result += n - target
        n = target
        if n < k:
            break
        result += 1
        n //= k
    return result


print(solve(n, k))
