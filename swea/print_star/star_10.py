import sys

# 재귀적으로 확장하는 구조이므로 3개의 재귀를 사용
def print_star(n):
    if n == 1:
        return "*"
    else:
        string = ""
        string += "*" + print_star(n - 1)

        return string


print(print_star(27))