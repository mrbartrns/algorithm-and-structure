# 징검다리
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start = 1
    end = distance
    while start <= end:
        mid = (start + end) // 2
        if check_cross(distance, rocks, n, mid):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


def check_cross(distance, rocks, n, mid):
    cnt = 0
    last = 0
    for rock in rocks:
        if rock - last >= mid:
            last = rock
            cnt += 1
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
