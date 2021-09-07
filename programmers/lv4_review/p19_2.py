# 숫자 블록
import math

INF = 987654321


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        n = INF
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0 and i // j <= 10000000:
                n = i // j
                break
        answer.append(n if n < INF else 1)
    return answer


if __name__ == "__main__":
    begin = 1
    end = 10
    print(solution(begin, end))