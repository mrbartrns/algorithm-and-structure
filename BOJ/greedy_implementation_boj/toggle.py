# BOJ 2138 전구와 스위치
"""N - 1 번째 전구를 다루기 위해서 N 번째 스위치를 조절한다."""
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def toggle_switch(idx, string):
    if string[idx] == "1":
        string[idx] = "0"
    else:
        string[idx] = "1"


def get_minimum_count(zero, b, a):
    ret = INF
    count = 0
    if zero:
        count += 1
        toggle_switch(0, b)
        toggle_switch(1, b)
    for i in range(1, N):
        if b[i - 1] == a[i - 1]:
            continue
        count += 1
        toggle_switch(i - 1, b)
        toggle_switch(i, b)
        if i + 1 < N:
            toggle_switch(i + 1, b)
    if "".join(b) == "".join(a):
        return min(ret, count)
    return ret


N = int(si())

before = list(si().strip())
after = list(si().strip())

cnt1 = get_minimum_count(False, before[:], after[:])
cnt2 = get_minimum_count(True, before[:], after[:])
answer = min(cnt1, cnt2)
print(answer if answer < INF else -1)
