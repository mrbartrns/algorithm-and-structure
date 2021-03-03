# 뉴스 클러스터링
import sys

si = sys.stdin.readline


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    dic1 = make_set(str1)
    dic2 = make_set(str2)
    intersection = 0
    # 교집합 구하기 -> 교집합은 양쪽에 적어도 하나씩 다 있으므로 둘 중 하나만 검사하면 됨
    for key in dic1.keys():
        intersection += min(dic1.get(key, 0), dic2.get(key, 0))

    sum_sets = sum(dic1.values()) + sum(dic2.values()) - intersection

    if sum_sets == 0 and intersection == 0:
        res = 1
    else:
        res = intersection / sum_sets
    return int(res * 65536)


def make_set(string):
    ret = {}
    for i in range(1, len(string)):
        new_ = string[i - 1] + string[i]
        if (
            ord("A") <= ord(string[i - 1])
            and ord(string[i - 1]) <= ord("Z")
            and ord("A") <= ord(string[i])
            and ord(string[i]) <= ord("Z")
        ):
            ret[new_] = ret.get(new_, 0) + 1
    return ret


s1 = si().strip()
s2 = si().strip()
print(solution(s1, s2))
