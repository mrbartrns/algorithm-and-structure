# [카카오] 오픈채팅방


def solution(record):
    answer = []
    id_dict = {}
    for query in record:
        q = query.split(" ")
        if len(q) >= 3:
            id_dict[q[1]] = q[2]
    for query in record:
        q = query.split(" ")
        if q[0] == "Enter":
            answer.append(f"{id_dict[q[1]]}님이 들어왔습니다.")
        elif q[0] == "Leave":
            answer.append(f"{id_dict[q[1]]}님이 나갔습니다.")
    return answer


if __name__ == "__main__":
    record = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
    print(solution(record))