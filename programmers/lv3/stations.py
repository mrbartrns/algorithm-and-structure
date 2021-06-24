# 기지국 설치
def solution(n, stations, w):
    answer = 0
    start = 0
    dis = 2 * w + 1
    stations.sort()
    for i in range(len(stations)):
        left = stations[i] - 1 - w
        right = stations[i] - 1 + w
        if left <= start <= right:
            start = right + 1
            continue

        div = (left - start) // dis
        rest = (left - start) % dis
        if rest > 0:
            div += 1
        answer += div
        start = right + 1

    if start < n:
        div = (n - start) // dis
        rest = (n - start) % dis
        if rest > 0:
            div += 1
        answer += div
    return answer


if __name__ == "__main__":
    n = 11
    stations = [4, 11]
    w = 1
    print(solution(n, stations, w))
