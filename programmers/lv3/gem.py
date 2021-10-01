# [카카오] 보석 쇼핑
INF = 987654321


def solution(gems):
    s = set(gems)
    counts = {}
    left, right = 0, 0
    answer = [0, len(gems)]
    length = INF
    while right < len(gems):
        gem = gems[right]
        counts[gem] = counts.get(gem, 0) + 1
        right += 1
        if len(s) == len(counts):
            while left < right:
                gem = gems[left]
                if counts[gem] > 1:
                    counts[gem] -= 1
                elif length > right - left:
                    answer = [left + 1, right]
                    length = right - left
                    break
                else:
                    break
                left += 1
    return answer


if __name__ == "__main__":
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))