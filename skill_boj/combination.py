# BOJ 2004
import sys

si = sys.stdin.readline


# 실제로 값을 구하는 것이 아닌, 조합 내의 2와 5의 갯수중 작은값을 선택하여 구한다.
# 숫자를 바꿀때에는 항상 복사 후 진행하기
def get_counts(n, mod):
    counts = 0
    div = mod
    while div <= n:
        counts += n // div
        div *= mod
    return counts


a, b = map(int, si().split())
# print(get_counts(a, 5) - get_counts(b, 5) - get_counts(a - b, 5))
print(
    min(
        get_counts(a, 5) - get_counts(a - b, 5) - get_counts(b, 5),
        get_counts(a, 2) - get_counts(a - b, 2) - get_counts(b, 2),
    )
)


# def countNum(N, num):
#     count = 0
#     divNum = num
#     while( N >= divNum):
#         count = count + (N // divNum)
#         divNum = divNum * num
#     return count
# M, N = map(int, input().split())

# print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))
