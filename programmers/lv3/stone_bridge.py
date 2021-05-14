# 징검다리 건너기
"""
시간 초과 코드
def solution(stones, k):
    answer = 0
    idx = -1
    while True:
        step = 1
        if idx >= len(stones):
            answer += 1
            idx = 0

        while idx + step < len(stones) and step <= k and stones[idx + step] == 0:
            step += 1

        if step > k:
            break

        idx += step
        if idx < len(stones):
            stones[idx] -= 1

    return answer
"""


def solution(stones, k):
    answer = 0
    return answer


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))
