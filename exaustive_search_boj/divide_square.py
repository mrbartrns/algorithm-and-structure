# BOJ 1451
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, si().strip())))  # 이것도 한줄로 축약이 가능함


def solve(table, n, m):
    # Case 1. |||
    res = 0
    for i in range(1, m - 1):
        for j in range(i + 1, m):
            s1 = sum([table[a][b] for a in range(n) for b in range(i)])
            s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
            s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)

    # Case 2. || --
    for i in range(1, m):  # 가로분할
        for j in range(1, n):  # 세로 분할
            s1 = sum([table[a][b] for a in range(j) for b in range(i)])
            s2 = sum([table[a][b] for a in range(j) for b in range(i, m)])
            s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
            res = max(res, s1 * s2 * s3)

    # Case 3. -- ||
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(m)])
            s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
            s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)

    # Case 4. ==|
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(j)])
            s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
            s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)

    # Case 5. |==
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(n) for b in range(j)])
            s2 = sum([table[a][b] for a in range(i) for b in range(j, m)])
            s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)

    # Case 6. =
    for i in range(1, n - 1):
        for j in range(i, n):
            s1 = sum([table[a][b] for a in range(i) for b in range(m)])
            s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
            s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
            res = max(res, s1 * s2 * s3)
    return res


# sum을 이용하지 않고 배열에 저장한다면, 더 빠르게 해결이 가능하다.
print(solve(matrix, n, m))


"""
def solve(arr):
    res = 0
    if len(arr[0]) >= 3:
        for i in range(1, len(arr[0]) - 1):
            for j in range(i + 1, len(arr[0])):
                div = (i, j)
                # sum div1
                div1 = 0
                for k in range(len(arr)):
                    for l in range(div[0]):
                        div1 += arr[k][l]

                val[0] = div1

                # sum div2
                div2 = 0
                for k in range(len(arr)):
                    for l in range(div[0], div[1]):
                        div2 += arr[k][l]

                val[1] = div2

                # sum div3
                div3 = 0
                for k in range(len(arr)):
                    for l in range(div[1], len(arr[0])):
                        div3 += arr[k][l]

                val[2] = div3

                print("val:", val)
                res = max(res, val[0] * val[1] * val[2])

    if len(arr) >= 3:
        for i in range(1, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                div = (i, j)

                # sum div1
                div1 = 0
                for k in range(div[0]):
                    for l in range(len(arr[0])):
                        div1 += arr[k][l]
                val[0] = div1

                div2 = 0
                for k in range(div[0], div[1]):
                    for l in range(len(arr[0])):
                        div2 += arr[k][l]
                val[1] = div2

                div3 = 0
                for k in range(div[1], len(arr)):
                    for l in range(len(arr[0])):
                        div3 += arr[k][l]
                val[2] = div3

                print("val:", val)
                res = max(res, val[0] * val[1] * val[2])
    return res


print(solve(matrix))
"""