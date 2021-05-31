# BOJ 1107
import sys

si = sys.stdin.readline

enable = {str(i) for i in range(10)}
n = int(si())
m = int(si())
if m > 0:
    enable -= set(map(str, si().split()))  # 가능한 숫자들만 남기고 제거


def solve(n):
    # case 1
    min_cnt = abs(n - 100)

    # 500000만보다 크면서 모든 숫자를 거치는 1000000만까지 브루트 포스 진행
    for num in range(1000001):
        str_num = str(num)
        for j in range(len(str_num)):
            if str_num[j] not in enable:
                break
            elif j == len(str_num) - 1:
                min_cnt = min(min_cnt, abs(n - num) + len(str_num))
    return min_cnt


print(solve(n))