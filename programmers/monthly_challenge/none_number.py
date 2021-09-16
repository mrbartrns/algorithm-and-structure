# 없는 숫자 찾기


def solution(numbers):
    ret = 0
    s = set(numbers)
    for i in range(10):
        if i not in s:
            ret += i
    return ret


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 6, 7, 8, 0]
    print(solution(numbers=numbers))