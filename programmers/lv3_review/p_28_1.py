# [카카오] 징검다리 건너기
def check(mid, stones, k):
    cnt = 0
    for stone in stones:
        if stone - mid < 0:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True


def solution(stones, k):
    start = 1
    end = max(stones)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if check(mid, stones, k):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))