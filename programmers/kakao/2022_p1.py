def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ids = {}
    for nickname in id_list:
        ids[nickname] = ids.get(nickname, set())
    for r in report:
        from_id, to_id = r.split(" ")
        ids[to_id].add(from_id)
    for i in range(len(id_list)):
        nickname = id_list[i]
        for j in ids.keys():
            if len(ids[j]) >= k and nickname in ids[j]:
                answer[i] += 1

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))
