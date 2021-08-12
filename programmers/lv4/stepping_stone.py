# 징검다리 (4단계)
def solution(distance, rocks, n):
    start = 1
    end = distance
    answer = 0
    rocks.sort()
    while start <= end:
        mid = (start + end) // 2
        if check(mid, distance, rocks, n):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


def check(mid, distance, rocks, n):
    cnt = 0
    last = 0
    for i in range(len(rocks)):
        if (rocks[i] - last) - mid >= 0:
            last = rocks[i]
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
