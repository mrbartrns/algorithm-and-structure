# 순위 검색


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
        print(int(q[4]))
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
