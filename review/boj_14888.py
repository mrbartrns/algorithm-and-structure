# BOJ 14888
# 8번 이상으로는 백트래킹 사실상 불가능
import sys
from itertools import permutations

si = sys.stdin.readline
n = int(si())
s = 0
numbers = list(map(int, si().split()))
o = list(map(int, si().split()))
op_ = []
values = []
MAX = -1e15
MIN = 1e15

# 연산자 삽입하기
for i in range(4):
    for _ in range(o[i]):
        op_.append(i)

# 연산자 순열 만들기
ops_list = list(permutations(op_))

# 첫 값을 저장하기
for ops in ops_list:
    s = numbers[0]
    for i in range(1, n):
        if ops[i - 1] == 0:
            s += numbers[i]
        elif ops[i - 1] == 1:
            s -= numbers[i]
        elif ops[i - 1] == 2:
            s *= numbers[i]
        else:
            if s < 0:
                s = -(abs(s) // numbers[i])  # 여기 문제
            else:
                s //= numbers[i]
    if s > MAX:
        MAX = s
    if s < MIN:
        MIN = s

print(MAX)
print(MIN)