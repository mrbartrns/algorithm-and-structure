# BOJ 1451
import sys

si = sys.stdin.readline


def solve(n, m, table):
    res = 0
    # case 1 ||| -> n 또는 m이 너무 작을 때에는(1일때) for문 진입을 하지 않는다.
    for i in range(1, m - 1):
        for j in range(i, m):
            # 이렇게 쓰는 형태 잘 익히기 [] 리스트(iterator) 내부에 요소의 범위 적어두기
            s1 = sum([table[a][b] for a in range(n) for b in range(i)])
            s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
            s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)

    # case 2 |==
    for i in range(1, n):
        for j in range(1, m):  # 선이 아닌 범위라고 생각해야함
            s1 = sum([table[a][b] for a in range(n) for b in range(j)])
            s2 = sum([table[a][b] for a in range(i) for b in range(j, m)])
            s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)

    # case 3 ==|
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(j)])
            s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
            s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)
    # case 4 ㅗ
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(j)])
            s2 = sum([table[a][b] for a in range(i) for b in range(j, m)])
            s3 = sum([table[a][b] for a in range(i, n) for b in range(m)])

    # case 5 ㅜ
    for i in range(1, n):
        for j in range(1, m):
            s1 = sum([table[a][b] for a in range(i) for b in range(m)])
            s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
            s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
            res = max(res, s1 * s2 * s3)

    # case 6 ===
    for i in range(1, n - 1):
        for j in range(i, n):
            s1 = sum([table[a][b] for a in range(i) for b in range(m)])
            s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
            s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
            res = max(res, s1 * s2 * s3)
    return res


n, m = map(int, si().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, si().strip())))

print(solve(n, m, matrix))