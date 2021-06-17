# 입국 심사
# 이분 탐색의 경우 어떠한 기준값이 있어야 한다 -> 그 기준을 계속해서 움직여야 하므로
"""
입국 심사를 기다리는 사람 수 n, 각 심사관 한 명이 심사하는데 걸리는 시간이 담긴 배열 times
심사관당 맏을 수 있는 입국자 수 = 추정 시간 값 / 각 심사관 별 심사 시간
시간을 기준으로 특정 시간을 주고 그 시간 내에 해결이 가능한 지 검사한 다음 이분탐색으로 가능한 시간 찾기
"""


def solution(n, times):
    times.sort()
    min_value = 1
    max_value = times[-1] * n
    answer = max_value
    while min_value <= max_value:
        mid = (min_value + max_value) // 2
        s = 0
        for i in range(len(times)):
            # 심사관당 맡을 수 있는 입국자 수
            s += mid // times[i]
        if n > s:
            min_value = mid + 1
        else:
            answer = min(answer, mid)
            max_value = mid - 1
    return answer


if __name__ == "__main__":
    n = 6
    arr = [7, 10]
    print(solution(n, arr))
