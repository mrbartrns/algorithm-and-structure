# 입국심사
"""
단위 변경하기 -> 문제에서 구하는것은 최소 시간이고, 사람수가 주어졌으므로 사람수와 시간간의 관계 표현하기
처리할 수 있는 사람의 수 = 주어진 특정 시간 (시간) // 각 심사위원이 한사람을 처리하는데 걸리는 시간 (시간 / 명)
주어진 시간 내에 n명을 모두 처리할 수 있다면 -> 시간을 줄여보기
그렇지 않다면 시간 늘리기
시간 범위의 최댓값은? 가장 오래 걸리는 심사위원 * n
시간 범위의 최댓값은 1
"""


def solution(n, times):
    times.sort()
    start = 1
    end = times[-1] * n
    answer = end + 1
    while start <= end:
        val = 0
        mid = (start + end) // 2
        for i in range(len(times)):
            val += mid // times[i]

        if val >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))
