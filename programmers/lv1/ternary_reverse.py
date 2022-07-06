def solution(n):
    ternary_value = get_ternary_value(n)[::-1]
    return int(ternary_value, 3)


def get_ternary_value(n):
    ret = ""
    while n > 0:
        ret = str(n % 3) + ret
        n //= 3
    return ret


n = 125
print(solution(n))
