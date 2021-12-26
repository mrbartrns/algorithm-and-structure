"""
원장선생님은 모든 보석을 N명의 학생들에게 나누어 주려고 한다. 보석을 받지 못하는 학생들이 있어도 된다.
질투심이 최소가 되도록 보석을 나누어 주어야 한다.
구해야 하는 값: 질투심의 최솟값 (질투심의 범위는 구해야 하는 값이면서 정렬되어 있는 값)
질투심은 보석을 한 사람당 나눠주는 개수가 된다.
질투심: 해당 질투심을 만족하기 위한 최소 인원 수 (질투심 // 해당 보석의 개수 + 1) 이 인원수가 인원 수를 초과 하면 안됨
나머지가 0이라면 1을 더하지 않아도 된다.
이분탐색에서 중요한 것: 단위 맞추기!
"""
# BOJ 2792 보석 상자
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def check(mid):
    count = 0
    for i in range(M):
        if arr[i] % mid == 0:
            count += arr[i] // mid
        else:
            count += (arr[i] // mid) + 1
    if count > N:
        return False
    return True


N, M = map(int, si().strip().split(" "))
arr = []
end = 0
for _ in range(M):
    a = int(si().strip())
    end = max(a, end)
    arr.append(a)
start = 1
answer = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
