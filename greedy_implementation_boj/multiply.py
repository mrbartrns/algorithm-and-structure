# 그리디 대표유형
# 그리디는 매번 최선의 선택을 하더라도 최종적으로 최적의 해를 보장받을 수 있는 경우에 사용할 수 있다.
arr = list(map(int, input()))


def solve(arr):
    ret = 0
    for i in range(len(arr)):
        if arr[i] <= 1 or ret <= 1:  # 1인경우도 곱하는것보다는 더하는 것이 더 크다.
            ret += arr[i]
        else:
            ret *= arr[i]
    return ret


print(solve(arr))