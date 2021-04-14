# BOJ 5639
import sys

si = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# 외부에서 참조하는것보다는 지역변수를 만들어 저장하여 사용하는것이 빠르다
def solve(start, end):
    if start > end:
        return
    idx = start + 1
    root = tree[start]
    while idx <= end:
        if tree[idx] > root:
            break
        idx += 1
    solve(start + 1, idx - 1)
    solve(idx, end)
    print(root)


tree = []
# tree = [50, 30, 24, 5, 28, 45, 98, 52, 60]
while True:
    try:
        tree.append(int(si()))
    except:
        break

solve(0, len(tree) - 1)
