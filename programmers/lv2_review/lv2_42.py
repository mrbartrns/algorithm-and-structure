# 점프와 순간 이동
# dp로 해결할 수 있으나 시간 너무 오래 걸림


def solution(n):
    ans = 0
    if n == 0:
        return ans
    if n % 2 == 1:
        ans = 1
    ans += solution(n // 2)
    return ans


n = 1000000000
print(solution(n))