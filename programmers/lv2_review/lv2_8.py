# 삼각달팽이
# imp
def solution(n):
    arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    ans = []
    top = 1
    btm = n
    left = 1
    right = 0
    num = 1
    MAX = (n * (n + 1)) // 2
    state = 0
    while num <= MAX:
        if state == 0:
            for i in range(top, btm + 1):
                arr[i][left] = num
                num += 1
            left += 1
            top += 1
            state = 1

        elif state == 1:
            for i in range(left, btm - right + 1):
                arr[btm][i] = num
                num += 1
            btm -= 1
            state = 2

        elif state == 2:
            for i in range(btm, top - 1, -1):
                arr[i][i - right] = num
                num += 1
            right += 1
            top += 1
            state = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] > 0:
                ans.append(arr[i][j])

    return ans


print(solution(5))