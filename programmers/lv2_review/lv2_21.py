# 카펫
def solution(brown, yellow):
    tot = brown + yellow
    for x in range(2, tot + 1):
        y = tot // x
        if x * y == tot and (x + y - 2) * 2 == brown and (x - 2) * (y - 2) == yellow:
            return [x, y] if x > y else [y, x]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))