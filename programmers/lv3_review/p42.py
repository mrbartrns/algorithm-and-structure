# 풍선 터트리기
# https://yabmoons.tistory.com/576 (해설)
def solution(a):
    if len(a) <= 2:
        return len(a)
    arr = []
    answer = 0
    for i in range(len(a)):
        arr.append((a[i], i))
    arr.sort(key=lambda x: x[0])
    f_idx = min(arr[0][1], arr[1][1])
    s_idx = max(arr[0][1], arr[1][1])
    for i in range(2, len(arr)):
        cur_idx = arr[i][1]
        if f_idx < cur_idx < s_idx:
            continue
        answer += 1
        f_idx = min(f_idx, cur_idx)
        s_idx = max(cur_idx, s_idx)
    return answer + 2


if __name__ == "__main__":
    a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
    print(solution(a))
