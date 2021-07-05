# 숫자 게임
def solution(a, b):
    a.sort()
    b.sort()
    idx = 0
    cnt = 0
    for i in range(len(a)):
        while idx < len(b) and b[idx] <= a[i]:
            idx += 1

        if idx < len(b) and b[idx] > a[i]:
            cnt += 1
            idx += 1

        if idx >= len(b):
            break
    return cnt


if __name__ == "__main__":
    a = [5, 1, 3, 7]
    b = [2, 2, 6, 8]
    print(solution(a, b))
