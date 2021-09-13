# [카카오] 순위 검색
from bisect import bisect_left

table = [
    ["-", "cpp", "java", "python"],
    ["-", "backend", "frontend"],
    ["-", "junior", "senior"],
    ["-", "chicken", "pizza"],
]


def get_subset(idx, arr, q_set, value_dict):
    if idx == 4:
        value_dict["".join(arr)].append(int(q_set[4]))
        return
    get_subset(idx + 1, arr + [q_set[idx]], q_set, value_dict)
    get_subset(idx + 1, arr + ["-"], q_set, value_dict)


def backtrack(idx, ret: dict, arr):
    if idx == len(table):
        ret["".join(arr)] = []
        return
    for i in range(len(table[idx])):
        arr.append(table[idx][i])
        backtrack(idx + 1, ret, arr)
        arr.pop()


def solution(info, query):
    value_dict = {}
    answer = []
    backtrack(0, value_dict, [])
    for q in info:
        q_set = q.split(" ")
        get_subset(0, [], q_set, value_dict)

    for key in value_dict.keys():
        value_dict[key].sort()

    for q in query:
        q_set = q.split(" ")
        q1, q2, q3, q4, score = q_set[0], q_set[2], q_set[4], q_set[6], int(q_set[7])
        answer.append(
            len(value_dict[q1 + q2 + q3 + q4])
            - bisect_left(value_dict[q1 + q2 + q3 + q4], score)
        )
    return answer


if __name__ == "__main__":
    info = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ]
    query = [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ]
    print(solution(info, query))