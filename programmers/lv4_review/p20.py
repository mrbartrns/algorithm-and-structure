# 숫자 블록
import math

INF = 10000000


def solution(begin, end):
    ret = []
    for number in range(begin, end + 1):
        if number == 1:
            ret.append(0)
            continue
        s = 1
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                s = number // i
                if s <= INF:
                    break
        ret.append(s if s <= INF else 1)

    return ret


if __name__ == '__main__':
    begin = 1
    end = 10
    print(solution(begin, end))
