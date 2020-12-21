# 계단 오르기
import sys


def get_step_memo(n):
    arr = [1, 1, 2]
    i = 3
    while i <= n:
        val = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000
        arr.append(val)
        i += 1
    return arr[n]


n = int(sys.stdin.readline())
print(get_step_memo(n))


def get_step(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        val = 0
        val = get_step(n - 1) + get_step(n - 2) + get_step(n - 3)
        return val


"""
def get_step(n, counts, k=0):
    if k == n:
        counts[0] += 1
        counts[0] %= 1000
        return
    else:
        if k + 1 <= n:
            get_step(n, counts, k + 1)
        if k + 2 <= n:
            get_step(n, counts, k + 2)
        if k + 3 <= n:
            get_step(n, counts, k + 3)


counts = [0]
# get_step(5, counts)
n = int(sys.stdin.readline())
get_step(n, counts)
print(counts[0])
"""
"""
[1, 2, 3]으로 이루어진 배열에서 몇개를 꺼내어 부분집합을 만든다.
이 부분집합의 합이 5라면, 멈춘다.
"""