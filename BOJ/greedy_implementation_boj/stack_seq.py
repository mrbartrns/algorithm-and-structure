# BOJ 1874
import sys

"""
스택에 푸시하는 순서는 반드시 오름차순 
1부터 n까지의 숫자
1 2 3 4
1 2 3
1 2
1 2 5 6
1 2 5 7
1 2 5 7 8
4 3 6 8 7 5 2 1 
스택에 넣은 뒤 pop하여 그것을 정답 배열에 추가해야 함
"""
# 배열이 다르면 no만 출력해야하므로 과정을 배열에 저장
si = sys.stdin.readline
n = int(si())
ans = []
arr = []
stack = []
process = []
idx = 0
for _ in range(n):
    el = int(si())
    ans.append(el)

for i in range(1, n + 1):
    while stack and stack[-1] == ans[idx]:
        u = stack.pop()
        arr.append(u)
        process.append("-")
        idx += 1
    if not stack or stack[-1] != ans[idx]:
        stack.append(i)
        process.append("+")

while stack:
    u = stack.pop()
    process.append("-")
    arr.append(u)

if ans == arr:
    print("\n".join(process))
else:
    print("NO")