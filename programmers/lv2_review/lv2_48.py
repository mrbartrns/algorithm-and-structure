# 오픈채팅방


def solution(record):
    ids = {}
    res = []
    for i in range(len(record)):
        temp = list(record[i].split())
        if temp[0] == "Enter" or temp[0] == "Change":
            ids[temp[1]] = temp[2]
    for i in range(len(record)):
        temp = list(record[i].split())
        script = ""
        if temp[0] == "Enter":
            script = ids[temp[1]] + "님이 들어왔습니다."
            res.append(script)
        elif temp[0] == "Leave":
            script = ids[temp[1]] + "님이 나갔습니다."
            res.append(script)
    return res


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
print(solution(record))