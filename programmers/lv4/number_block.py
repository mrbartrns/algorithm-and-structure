# 숫자 블록
import math

MAX_VALUE = 10000000


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        num = 1
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                num = i // j
                if num <= MAX_VALUE:
                    break
        answer.append(num if num <= MAX_VALUE else 1)
    return answer


if __name__ == '__main__':
    begin = 24000000
    end = 24000002
    print(solution(begin, end))
