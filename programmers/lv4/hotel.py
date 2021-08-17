# [카카오인턴] 호텔 방 배정
import sys

sys.setrecursionlimit(200001)


def solution(k, room_number):
    parents = {}
    answer = []
    for room in room_number:
        check_in = get_parent(parents, room)
        answer.append(check_in)
        union_parent(parents, check_in, check_in + 1)
    return answer


def get_parent(parents, a):
    parents[a] = parents.get(a, a)
    if parents[a] == a:
        return a
    parents[a] = get_parent(parents, parents[a])
    return parents[a]


def union_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a > b:
        parents[b] = a
    else:
        parents[a] = b


if __name__ == '__main__':
    k = 10 ** 12
    room_number = [i for i in range(10 ** 10, 10 ** 10 + 200001)]
    print(solution(k, room_number))
