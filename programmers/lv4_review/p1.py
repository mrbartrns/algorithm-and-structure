# 징검다리 (이분탐색)
def solution(distance, rocks, n):
    start = 1
    end = distance
    answer = 0
    rocks.sort()
    while start <= end:
        mid = (start + end) // 2
        if can_cross(distance, rocks, n, mid):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


def can_cross(distance, rocks, n, mid):
    cnt = 0
    last = 0
    for rock in rocks:
        if rock - last >= mid:
            cnt += 1
            last = rock
    if distance - last < mid:
        return False
    if cnt < len(rocks) - n:
        return False
    return True


if __name__ == '__main__':
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2
    print(solution(distance, rocks, n))
