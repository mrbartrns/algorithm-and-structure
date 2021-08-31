# 선입 선출 스케쥴링
# 총 작업이 끝나는 시간 = (최소 작업시간 * (작업량 - 코어 갯수)) // 코어 수
INF = 987654321


def solution(n, cores):
    if n <= len(cores):
        return n

    start = 1
    end = 10000
    while start <= end:
        mid = (start + end) // 2
        count = count_work(mid, cores)
        m = 0
        if count >= n:
            end = mid - 1
            time = mid
            m = count
        else:
            start = mid + 1





def count_work(mid, cores):
    count = len(cores)
    for core in cores:
        count += mid // core
    return count
