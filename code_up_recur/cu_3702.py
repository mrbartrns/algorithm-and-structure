import sys

# 파스칼의 삼각형 구하기


def pascal(r, c):
    if r == 1:
        return 1
    else:
        sum_val = 0
        i = 1
        while i <= c:
            sum_val += pascal(r - 1, i)
            i += 1
        return sum_val


# get memoization of pascal triangle


def pascal_memo(r, c):
    arr = [[1 for _ in range(c)]]
    i = 0
    while len(arr) < r:
        temp = []
        j = 0
        sum_val = 0
        while j < c:
            sum_val += arr[i][j]
            sum_val %= 100000000
            temp.append(sum_val)
            j += 1
        arr.append(temp)
        i += 1
    return arr[-1][-1]


# r, c = map(int, sys.stdin.readline().split())
# print(pascal_memo(r, c))

print(pascal_memo(44, 10))