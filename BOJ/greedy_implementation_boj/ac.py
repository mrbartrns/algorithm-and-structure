# BOJ 5430
import sys
from collections import deque

si = sys.stdin.readline


def solve(operators: str, queue: deque) -> list:
    reverse = False
    for op in operators:
        if op == "R":
            reverse = not reverse
        elif op == "D":
            if queue and not reverse:
                queue.popleft()
            elif queue and reverse:
                queue.pop()
            else:
                return [-1]
    if reverse:
        return list(reversed(queue))
    return list(queue)


t = int(si())
for _ in range(t):
    ops = si().strip()
    n = int(si())
    arr_str = si().strip()
    arr = list(map(int, arr_str[1:-1].split(","))) if arr_str != "[]" else []
    que = deque(arr)
    val = solve(ops, que)
    ans = "["
    ans += ",".join(list(map(str, val)))
    ans += "]"
    print(ans) if val != [-1] else print("error")