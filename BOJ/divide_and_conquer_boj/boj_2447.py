# BOJ 2447
n = 27


# 첫번째 방법
def solve(x, y, n):
    """
    @type x: row
    @type y: col
    @type n: scale
    """
    if (x // n) % 3 == 1 and (y // n) % 3 == 1:
        print(" ", end="")
        return
    if n // 3 == 0:
        print("*", end="")
    else:
        solve(x, y, n // 3)


for i in range(n):
    for j in range(n):
        solve(i, j, n)
    print()

# 두번째 방법
arr = [[" " for _ in range(n)] for _ in range(n)]


def divide(x, y, n):
    if n == 1:
        arr[x][y] = "*"
        return

    # 주어진 그림을 9등분 한것과 동일하다 > 여태 해온것처럼!
    # 이 방법 완벽히 이해하기 (뜻)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 항상 등분의 가운데가 된다
                continue  # 아무것도 하지 말것
            divide(x + i * (n // 3), y + j * (n // 3), n // 3)  # 시작 좌표


divide(0, 0, n)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
