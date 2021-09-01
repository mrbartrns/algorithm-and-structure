# 선입 선출 스케쥴링
"""
이분탐색의 매개변수: 시간
우리는 for 문을 이용하여 반복문을 순회하면서 모든 값을 배열의 길이만큼 더하기 때문에 하나의 코어가 갖는 최대 시간을
설정하면 된다.
반대로 접근하기: 더했을 때 총 걸리는 시간이 min(cores) * n이 되기위해서는 어떻게 되야 하는지?
즉, start = min(cores) * n // len(cores)
    end = max(cores) * n // len(cores)
"""
INF = 987654321


def solution(n, cores):
    min_core, max_core = INF, 0
    for core in cores:
        min_core = min(core, min_core)
        max_core = max(core, max_core)
    start = min_core * n // len(cores)
    end = max_core * n // len(cores)
    while start <= end:
        mid = (start + end) // 2
        work_done = 0
        available = 0
        for core in cores:
            # mid 시간 도달 직전까지 작업의 양 측정
            work_done += (mid // core) + 1
            if mid % core == 0:
                # 현재 비어있기 때문에
                available += 1
                work_done -= 1

        # 끝난 작업의 양이 n보다 크거나 같을 경우, 더 이상 할 수 있는 일이 없다.
        if work_done >= n:
            end = mid
        # 총 수행 작업 + 넣을 수 있는 공간이 n보다 작다면, 총 할 수 있는 일의 양이 n 미만이다.
        elif work_done + available < n:
            start = mid + 1
        else:
            for i in range(len(cores)):
                core = cores[i]
                if mid % core == 0:
                    work_done += 1
                if work_done == n:
                    return i + 1


if __name__ == '__main__':
    n = 6
    cores = [1, 2, 3]
    print(solution(n, cores))
