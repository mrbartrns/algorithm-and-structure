# 다음 큰 숫자
def solution(n):
    n_bin = get_bin(n)
    n_1 = get_one(n_bin)
    num = n
    while True:
        num += 1
        num_bin = get_bin(num)
        num_1 = get_one(num_bin)
        if n_1 == num_1:
            return num


def get_bin(n):
    res = ""
    if n == 0:
        return res

    if n % 2 == 0:
        res = get_bin(n // 2) + "0"
    else:
        res = get_bin(n // 2) + "1"
    return res


def get_one(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == "1":
            cnt += 1
    return cnt