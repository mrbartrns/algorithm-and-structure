# 멀쩡한 사각형
def solution(w, h):
    return w * h - (w + h - gcd(w, h))


def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    return gcd(b, a % b)
