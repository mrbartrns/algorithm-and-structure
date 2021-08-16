# 선입선출 스케쥴링 (파라메트릭 서치)
INF = 987654321


def solution(n, cores):
    if n <= len(cores):
        return n
    min_core = min(cores)

    answer = 0
    start = n // len(cores) * min_core
    end = start * n
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        available = 0
        for core in cores:
            cnt += (mid // core) + 1
            if mid % core == 0:
                available += 1
                cnt -= 1

        if cnt >= n:
            end = mid
        elif cnt + available < n:
            start = mid + 1
        else:
            for i in range(len(cores)):
                if mid % cores[i] == 0:
                    cnt += 1

                if cnt == n:
                    return i + 1
    return answer


if __name__ == '__main__':
    n = 6
    cores = [1, 2, 3]
    print(solution(n, cores))
