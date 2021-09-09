# 선입 선출 스케쥴링
def solution(n, cores):
    start = min(cores) * n // len(cores)
    end = start * n
    while start <= end:
        mid = (start + end) // 2
        work_done = 0
        available = 0
        for core in cores:
            work_done += (mid // core) + 1
            if mid % core == 0:
                work_done -= 1
                available += 1

        if work_done >= n:
            end = mid - 1
        elif available + work_done < n:
            start = mid + 1
        else:
            for i in range(len(cores)):
                core = cores[i]
                if mid % core == 0:
                    work_done += 1
                if work_done == n:
                    return i + 1


if __name__ == "__main__":
    n = 6
    cores = [1, 2, 3]
    print(solution(n, cores))
