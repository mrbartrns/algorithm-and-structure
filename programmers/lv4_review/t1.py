# 테스트1 - 지형 변경


def solution(land, P, Q):
    tot = 0
    arr = []
    for i in range(len(land)):
        for j in range(len(land)):
            arr.append(land[i][j])
            tot += land[i][j]
    arr.sort()
    s = (tot - arr[0] * len(arr)) * Q
    answer = s
    for i in range(1, len(arr)):
        up = (arr[i] - arr[i - 1]) * i * P
        down = (arr[i] - arr[i - 1]) * (len(arr) - i) * Q
        s += up - down
        answer = min(answer, s)

    return answer


if __name__ == "__main__":
    land = [[1, 2], [2, 3]]
    p = 3
    q = 2
    print(solution(land, p, q))