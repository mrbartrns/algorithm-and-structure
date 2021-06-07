# 보석 쇼핑
def solution(gems):
    answer = []
    counts = {}
    maximum_value = 987654321
    kinds = len(set(gems))
    left, right = 0, 0
    while right < len(gems):
        gem = gems[right]
        counts[gem] = counts.get(gem, 0) + 1
        right += 1
        if len(counts) == kinds:
            while left < right:
                gem = gems[left]
                if counts[gem] > 1:
                    counts[gem] -= 1
                    left += 1
                elif maximum_value > right - left:
                    maximum_value = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break
    return answer


if __name__ == "__main__":
    arr = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(arr))
