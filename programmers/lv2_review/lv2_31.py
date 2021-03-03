# 숫자의 표현
def solution(n):
    left = 0
    right = 0
    cnt = 0
    value = 0
    while True:
        if value >= n:
            if value == n:
                print(left, right)
                cnt += 1
            left += 1
            value -= left

        elif value < n:
            right += 1
            value += right

        if right > n:
            break
    return cnt


n = 15
print(solution(n))