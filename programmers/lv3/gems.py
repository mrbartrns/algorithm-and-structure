# [카카오] 보석 쇼핑
INF = 987654321


def solution(gems):
    counts = {}
    s = set(gems)
    left, right = 0, 0
    length = 987654321
    answer = [1, len(gems)]
    while right < len(gems):
        gem = gems[right]
        counts[gem] = counts.get(gem, 0) + 1
        right += 1
        if len(s) == len(counts):
            while left < right:
                gem = gems[left]
                if counts[gem] > 1:
                    counts[gem] -= 1
                    left += 1
                elif right - left < length:
                    length = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break
    return answer


if __name__ == "__main__":
    gems = ["AA", "AB", "AC", "AA", "AC"]
    print(solution(gems))