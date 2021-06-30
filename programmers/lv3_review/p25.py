# [카카오] 징검다리 건너기
"""
0 이하인 값이 연속되게 k개 이상 나온다면 값을 줄여나가기
문제를 정확하게 이해하고 코드 작성하는 습관 들이기
"""


def solution(stones, k):
    start = 1
    end = max(stones)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if check(mid, stones, k):
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer


def check(value, stones, k):
    cnt = 0
    for i in range(len(stones)):
        # 0과 같을 경우 현재 번째 인원까지 뛰고 난 다음에 0이 되었다는 뜻이므로 뛸 수 있다는 뜻이다.
        if stones[i] - value < 0:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))
