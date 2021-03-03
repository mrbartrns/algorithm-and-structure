# 쿼드압축 후 개수 세기
def solution(arr):
    ans = [0, 0]
    divide(0, 0, len(arr), arr, ans)
    return ans


def divide(x, y, k, arr, ans):
    if k == 1:
        ans[arr[x][y]] += 1
        return

    check = arr[x][y]
    flag = True
    for i in range(x, x + k):
        for j in range(y, y + k):
            if arr[i][j] != check:
                flag = False
                break

    if flag:
        ans[check] += 1
    else:
        for i in range(2):
            for j in range(2):
                divide(x + (k // 2) * i, y + (k // 2) * j, k // 2, arr, ans)


# arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
arr = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
]
print(solution(arr))