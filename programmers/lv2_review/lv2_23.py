# 순위 검색
arr = [5, 8, 15, 21, 26]

"""
def solution(info, query):
    answer = []
    u = [info[i].split(" ") for i in range(len(info))]
    for i in range(len(u)):
        u[i][4] = int(u[i][4])
    u.sort(key=lambda x: x[4])

    for i in range(len(query)):
        cnt = 0
        temp = query[i].split(" ")
        q = [temp[i] for i in range(len(temp)) if temp[i] != "and"]
        # print(q)
        idx = search(u, int(q[4]))
        for j in range(idx, len(u)):
            q1 = u[j][0] == q[0] if q[0] != "-" else True
            q2 = u[j][1] == q[1] if q[1] != "-" else True
            q3 = u[j][2] == q[2] if q[2] != "-" else True
            q4 = u[j][3] == q[3] if q[3] != "-" else True
            if q1 and q2 and q3 and q4:
                cnt += 1
        answer.append(cnt)

    return answer

"""


def search(arr, target):
    start = 0
    end = len(arr) - 1
    ans = len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans


def solution(info, query):
    answer = []
    ref = {}
    for i in range(len(info)):
        temp = info[i].split(" ")
        dfs("", 0, len(temp) - 1, temp, ref)
    for i in list(ref.keys()):
        ref[i].sort()
    for i in range(len(query)):
        cnt = 0
        temp = query[i].split(" ")
        q = [temp[i] for i in range(len(temp)) if temp[i] != "and"]
        qu = "".join(q[:-1])
        if ref[qu]:
            idx = len(ref[qu])
            cnt = idx
            score = int(q[-1])
            idx = search(ref[qu], score)
            answer.append(cnt - idx)
        else:
            answer.append(cnt)
    return answer


"""
    for i in range(len(query)):
        tot = ref
        cnt = 0
        temp = query[i].split(" ")
        q = [temp[i] for i in range(len(temp)) if temp[i] != "and"]
        q1 = q[0] if q[0] != "-" else None
        q2 = q[1] if q[1] != "-" else None
        q3 = q[2] if q[2] != "-" else None
        q4 = q[3] if q[3] != "-" else None
        score = int(q[-1])
        if q1:
            tot = tot & languages[q1]
        if q2:
            tot = tot & positions[q2]
        if q3:
            tot = tot & careers[q3]
        if q4:
            tot = tot & foods[q4]
        for people in tot:
            if scores[people] >= score:
                cnt += 1
        answer.append(cnt)
"""


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