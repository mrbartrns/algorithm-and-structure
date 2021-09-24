# [카카오] 순위 검색
from bisect import bisect_left

table = [
    ["-", "cpp", "java", "python"],
    ["-", "backend", "frontend"],
    ["-", "junior", "senior"],
    ["-", "chicken", "pizza"],
]

all_set = {}


def get_subset(idx, string, arr):
    if idx == len(arr) - 1:
        all_set[string].append(int(arr[-1]))
        return
    get_subset(idx + 1, string + arr[idx], arr)
    get_subset(idx + 1, string + "-", arr)


def backtrack(idx, string):
    if idx == len(table):
        all_set[string] = []
        return
    for i in range(len(table[idx])):
        backtrack(idx + 1, string + table[idx][i])


def solution(info, query):
    answer = []
    backtrack(0, "")
    for sentence in info:
        get_subset(0, "", sentence.split(" "))
    for q in all_set:
        all_set[q].sort()
    for q in query:
        q_arr = q.split(" ")
        queryset = ""
        score = int(q_arr[-1])
        for i in range(0, len(q_arr) - 1, 2):
            queryset += q_arr[i]
        answer.append(len(all_set[queryset]) - bisect_left(all_set[queryset], score))
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