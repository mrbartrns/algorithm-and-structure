# 카카오 메뉴 리뉴얼
def solution(orders, course):
    res = []
    dic = {}
    for c in orders:
        ret = get_sub_seq(c)
        for i in range(1, len(ret)):
            dic[ret[i]] = dic.get(ret[i], 0) + 1
    items = sorted(dic.items(), key=lambda x: (len(x[0]), -x[1]))
    for j in course:
        temp = []
        for key, value in items:
            if len(key) == j and value > 1 and (not temp or value == dic[temp[0]]):
                temp.append(key)
        res.extend(temp)

    res.sort()
    return res


def permutation(s, idx, n, res, string):
    if idx == n:
        l_s = list(s)
        l_s.sort()
        res.append("".join(l_s))
        return

    permutation(s + string[idx], idx + 1, n, res, string)
    permutation(s, idx + 1, n, res, string)


def get_sub_seq(string):
    n = len(string)
    res = []
    permutation("", 0, n, res, string)
    res.sort(key=lambda x: len(x))
    return res


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
