# 최솟값 만들기(그리디)
def solution(a, b):
    a.sort()
    b.sort(reverse=True)
    n = len(a)
    s = 0
    for i in range(n):
        m = a[i] * b[i]
        s += m
    return s


a = [1, 4, 2]
b = [5, 4, 4]
print(solution(a, b))