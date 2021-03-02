# 가장 큰 수
def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(str_numbers)))


print(solution([6, 10, 2]))