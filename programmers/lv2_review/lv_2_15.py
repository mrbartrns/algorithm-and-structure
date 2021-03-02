# 과거 코드


def solution(name):
    answer = 0
    a_count = 0
    idx = -1
    not_a_count = 0
    # is_a = False
    # 이것은 갈아 치울 필요 없음
    for c in name:
        if ord(c) - ord("A") <= ord("Z") - ord(c):
            answer += ord(c) - ord("A")
            # print(ord(c) - ord("A"))
        else:
            answer += ord("Z") - ord(c) + 1
    # 여기서부터 수정 필요
    for i in range(1, len(name) + 1):
        pattern = "A" * i
        if name.find(pattern) != -1 and a_count < len(pattern):
            idx = name.find(pattern)
            not_a_count = idx
            a_count = len(pattern)
    not_a_count = idx - 1 if idx > 0 else 0
    if idx == -1:
        answer += len(name) - 1
    else:
        if a_count >= not_a_count:
            if idx == 0:
                if name[
                    len(name) - a_count : len(name)
                ] == "A" * a_count and a_count != len(name):
                    answer += len(name) - 1 - a_count
                else:
                    answer += len(name) - 1 - a_count + not_a_count + 1
            else:
                if (
                    idx + a_count == len(name)
                    and name[:a_count] != name[len(name) - a_count : len(name)]
                ):
                    answer += len(name) - 1 - a_count
                else:
                    answer += len(name) - 1 - a_count + not_a_count
        else:
            if (
                idx + a_count == len(name)
                and name[:a_count] != name[len(name) - a_count : len(name)]
            ):
                answer += len(name) - 1 - a_count
            else:
                answer += len(name) - 1

    return answer


"""
def solution(name):
    res, idx = 0, 0
    ords = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    while True:
        res += ords[idx]
        ords[idx] = 0
        if sum(ords) == 0:
            break
        left, right = 1, 1
        while ords[idx - left] == 0:
            left += 1
        while ords[idx + right] == 0:
            right += 1
        res += left if left < right else right
        idx -= left if left < right else right
    return res
"""

print(solution("JAN"))
