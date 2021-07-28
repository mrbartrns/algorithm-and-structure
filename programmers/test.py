def solution(a):
    if len(a) <= 2:
        return len(a)

    answer = 0
    arr = []
    for i in range(len(a)):
        arr.append((a[i], i))

    arr.sort()
    f_idx = min(arr[0][1], arr[1][1])
    s_idx = max(arr[0][1], arr[1][1])
    for i in range(2, len(arr)):
        if f_idx < arr[i][1] < s_idx:
            continue

        answer += 1
        f_idx = min(f_idx, arr[i][1])
        s_idx = max(s_idx, arr[i][1])
    return answer + 2


if __name__ == "__main__":
    a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
    print(solution(a))