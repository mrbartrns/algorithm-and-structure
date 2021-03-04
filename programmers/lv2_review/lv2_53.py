# n진수 게임
def divide(n, mod):
    res = ""
    if n == 0:
        return res
    if n % mod < 10:
        res = divide(n // mod, mod) + str(n % mod)
    else:
        res = divide(n // mod, mod) + chr(ord("A") + n % mod - 10)
    return res


def solution(n, t, m, p):
    number = 0
    string = "0"  # 0일때는 아무것도 안나옴
    ans = ""
    while len(string) <= t * m:
        string += divide(number, n)
        number += 1
    for i in range(len(string)):
        if p - 1 == i % m:
            ans += string[i]
        if len(ans) == t:
            break
    return ans