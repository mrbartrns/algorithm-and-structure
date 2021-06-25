# 보석 쇼핑
def solution(gems):
    answer = [1, len(gems)]
    left = 0
    right = 0
    s = set(gems)
    min_val = len(gems)
    counts = {}
    while right < len(gems):
        gem = gems[right]
        counts[gem] = counts.get(gem, 0) + 1
        right += 1

        if len(counts) == len(s):
            while left < right:
                gem = gems[left]
                if counts[gem] > 1:
                    counts[gem] -= 1
                    left += 1
                elif min_val > right - left:
                    min_val = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break
    return answer


if __name__ == "__main__":
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))
