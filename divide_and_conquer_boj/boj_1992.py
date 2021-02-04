# BOJ 1992
n = 8
arr = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1],
]

# 행렬을 분할정복하기 위한 기본 구조라고 생각해도 된다.
def divide(x, y, n):
    if n == 1:
        return str(arr[x][y])

    string = ""
    flag = True
    start = arr[x][y]  # 현재 좌표
    # n의 크기가 x보다 작을 수 있기 때문에 항상 범위에 대해서 생각해야 한다.
    # 배열을 다룰때에는 인덱스 에러에 조심한다.
    for i in range(x, x + n):
        for j in range(y, y + n):
            if start != arr[i][j]:
                flag = False
                break
    if flag:
        string += str(start)
    else:
        string = "("
        for i in range(2):
            for j in range(2):
                string += divide(x + i * (n // 2), y + j * (n // 2), n // 2)
        string += ")"
    return string


print(divide(0, 0, n))