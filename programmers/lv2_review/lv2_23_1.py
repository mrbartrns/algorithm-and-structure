# 순위 검색

from bisect import bisect_left


def solution(info, query):
    answer = []
    ref = {}

    # ref 정렬하는것 문제 없음
    for i in range(len(info)):
        temp = info[i].split(" ")
        # 주어지는 배열의 마지막 요소는 점수이므로
        end = len(temp) - 1
        dfs("", 0, end, temp, ref)

    for key in ref.keys():
        ref[key].sort()

    for i in range(len(query)):
        cnt = 0
        temp = query[i].split(" ")
        q = [temp[i] for i in range(len(temp)) if temp[i] != "and"]
        qu = "".join(q[:-1])
        score = int(q[-1])
        if ref[qu]:
            size = len(ref[qu])
            cnt = size - bisect_left(ref[qu], score)
            answer.append(cnt)
        else:
            answer.append(0)
    return answer


def dfs(s, idx, length, arr, dic):
    if idx == length:
        dic[s] = dic.get(s, []) + [int(arr[4])]
        return
    dfs(s + "-", idx + 1, length, arr, dic)
    dfs(s + arr[idx], idx + 1, length, arr, dic)


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