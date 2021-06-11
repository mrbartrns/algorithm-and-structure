# 큰수의 법칙
# 시간 복잡도를 최소한으로 간소화하면서 문제 해결하기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


# 하나의 세트 수열을 만들고, 그 수열의 값을 몫 만큼 곱하기 -> 나머지를 더하기
def solve(numbers, m, k):
    res = 0
    cnt = m
    numbers.sort()
    first, second = numbers[-1], numbers[-2]
    seq_sum = first * k + second
    res += (cnt // (k + 1)) * seq_sum
    cnt %= (k + 1)
    res += cnt * first
    return res


n, m, k = map(int, si().split())
arr = list(map(int, si().split()))
print(solve(arr, m, k))
