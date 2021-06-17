# 징검다리 건너기
"""
징검다리의 돌의 크기가 2억이기 때문에, 어떠한 추정치의 기준을 이것으로 잡아야 함
이분탐색의 경우 어떠한 단위의 자료형이 항상 정렬되어 있어야 함
돌의 크기는 인원수와 동일한 단위를 가짐
현재 인원수가 돌의 숫자보다 더 큰경우 -> 통과 불가
큰 경우가 k번을 넘어갈 경우 통과 할 수 없음 -> 그때의 최대 인원 구하기
현재 인원수가 돌의 숫자보다 더 작은 경우 -> 통과 가능
k 번 연속되는 경우를 구하기 위하여 새로운 함수 필요
이분 탐색의 구조: 어떤 값을 비교 -> 그 값을 이용하여 작업을 실행하는 2개의 구조로 나누어져 있음
"""


def solution(stones, k):
    start = 1
    end = 200000000
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if check(stones, mid, k):
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer


def check(stones, mid, k):
    cnt = 0
    for i in range(len(stones)):
        if stones[i] < mid:
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
