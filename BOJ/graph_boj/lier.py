# BOJ 1043 거짓말
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


def find_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    return a == b


def get_parent(arr, a):
    if arr[a] == a:
        return a
    arr[a] = get_parent(arr, arr[a])
    return arr[a]


N, M = map(int, si().split(" "))
parents = [i for i in range(N + 1)]
known = list(map(int, si().split(" ")))[1:]
parties = []
for _ in range(M):
    party = list(map(int, si().split(" ")))
    if party[0] > 1:
        for i in range(1, len(party) - 1):
            if not find_parent(parents, party[i], party[i + 1]):
                union_parent(parents, party[i], party[i + 1])
    parties.append(party[1:])
count = 0
for party in parties:
    check = True
    for i in range(len(party)):
        p = party[i]
        for q in known:
            if find_parent(parents, p, q):
                check = False
                break
        if not check:
            break
    if check:
        count += 1
print(count)
