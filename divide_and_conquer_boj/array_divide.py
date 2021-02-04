# BOJ 1780
import sys

si = sys.stdin.readline


n = 9
arr = [
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, -1, 0, 1, -1, 0, 1, -1],
    [0, -1, 1, 0, 1, -1, 0, 1, -1],
    [0, 1, -1, 1, 0, -1, 0, 1, -1],
]
"""
n = int(si())
arr = []
for _ in range(n):
    arr.append(list(map(int, si().split())))
"""
# 함수를 구성하기 어려울 것 같으면 쪼개기
def count(x, y, n):
    temp = arr[x][y]
    rtn = [0, 0, 0]
    for i in range(n):
        for j in range(n):
            if temp != arr[x + i][y + j]:
                rtn = divide(x, y, n)
                return rtn
    rtn[temp + 1] += 1
    return rtn


def divide(x, y, n):
    result = [0, 0, 0]
    temp = []
    for i in range(3):
        for j in range(3):
            temp = count(x + i * (n // 3), y + j * (n // 3), n // 3)
            result[0] += temp[0]
            result[1] += temp[1]
            result[2] += temp[2]
    return result


print("\n".join(list(map(str, count(0, 0, n)))))


# 내가 하려고 했던 방법 > 실제로 그래프를 쪼개서 그 그래프를 반환한 후 처리하는 방법
# 이사람이 한 방법 > 그래프를 쪼개지 않고 인덱스만 바꿔서 처리하는 방법
# 인덱싱 분할하는 법 완벽하게 기억하기
# 너무 내가 표면적으로만 접근하는 것이 아닌지?
# 분할 정복의 기본적인 틀 익히기
"""
def divide(x, y, n):
    if len(arr[0]) == 1:
        return arr

    start = arr[0][0]
    same = True
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if start != arr[i][j]:
                same = False
                break

    if same:
        return arr
    else:
        new = []
        for i in range(3):
            for j in range(3):
                new_arr = [
                    row[j * (n // 3) : (j + 1) * (n // 3)]
                    for row in arr[i * (n // 3) : (i + 1) * (n // 3)]
                ]
                print(new_arr)
                new += divide(new_arr, n // 3)
        return new
"""
