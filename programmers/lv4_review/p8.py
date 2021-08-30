# [호텔 방 배정]
import sys

sys.setrecursionlimit(200001)


def solution(k, room_number):
    parents = {}
    answer = []
    for room in room_number:
        r = get_parent(parents, room)
        answer.append(r)
        union_parent(parents, r, r + 1)
    return answer


def get_parent(parents, a):
    parents[a] = parents.get(a, a)
    if parents[a] == a:
        return a
    parents[a] = get_parent(parents, parents[a])
    return parents[a]


def union_parent(arr, a, b):
    a = get_parent(arr, a)
    b = get_parent(arr, b)
    if a < b:
        arr[a] = b
    else:
        arr[b] = a


if __name__ == '__main__':
    k = 10
    room_number = [1, 3, 4, 1, 3, 1]
    print(solution(k, room_number))
