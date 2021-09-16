# [카카오] 뉴스 클러스터링


def get_sum_set(set1, set2):
    cnt = 0
    ret = {}
    for key in set1:
        ret[key] = max(set1.get(key, 0), set2.get(key, 0))
    for key in set2:
        ret[key] = max(set1.get(key, 0), set2.get(key, 0))
    for key in ret:
        cnt += ret[key]
    return cnt


def get_intersection(set1, set2):
    cnt = 0
    for key in set1:
        cnt += min(set1.get(key, 0), set2.get(key, 0))
    return cnt


def get_subset(string):
    s_set = {}
    for i in range(len(string)):
        substring = string[i : i + 2]
        if len(substring) < 2:
            break
        check = True
        for c in substring:
            if ord(c) < ord("a") or ord(c) > ord("z"):
                check = False
                break
        if check:
            s_set[substring] = s_set.get(substring, 0) + 1
    return s_set


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1_set = get_subset(str1)
    s2_set = get_subset(str2)
    intersection_cnt = get_intersection(s1_set, s2_set)
    sum_cnt = get_sum_set(s1_set, s2_set)
    if sum_cnt == 0:
        return 65536
    answer = int((intersection_cnt / sum_cnt) * 65536)
    return answer


if __name__ == "__main__":
    str1 = "E=M*C^2"
    str2 = "e=m*c^2"
    print(solution(str1, str2))