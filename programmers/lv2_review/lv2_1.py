# 123 나라의 숫자
def solution(n):
    string = ""
    if n > 0:
        if n % 3 == 0:
            string = "4"
        elif n % 3 == 1:
            string = "1"
        else:
            string = "2"

        if n % 3 > 0:
            string = solution(n // 3) + string
        else:
            string = solution(n // 3 - 1) + string
    return string


n = int(input())
print(solution(n))