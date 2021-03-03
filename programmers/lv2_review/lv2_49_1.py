from itertools import permutations


def solution(relation):
    ans = 0
    has = set()
    dic = {}
    size = len(relation[0])
    for i in range(1, size):
        temp = list(permutations([j for j in range(size)], i))
        for keys in temp:
            string = ""
            for key in keys:
                string += str(key)
            dic[string] = []

    for i in range(len(relation)):
        for key in dic.keys():
            temp = []
            for c in key:
                idx = int(c)
                temp.append(relation[i][idx])
            dic[key].append(temp)

    for key in dic.keys():
        dic[key].sort()
    key_list = sorted(list(dic.keys()), key=lambda x: len(x))

    for key in key_list:
        flag = True
        for i in range(len(dic[key]) - 1):
            if dic[key][i] == dic[key][i + 1]:
                flag = False
                break
        if flag:
            for k in has:
                if key.find(k) > -1:
                    flag = False
                    break
        if flag:
            has.add(key)
            ans += 1

    print(has)

    return ans


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]

print(solution(relation))