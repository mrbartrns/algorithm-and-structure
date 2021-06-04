# 보석 쇼핑


def solution(gems):
    answer = []
    counts = {}
    kinds = len(set(gems))
    minimum = 987654321
    left, right = 0, 0
    while right < len(gems):
        cur_right = gems[right]
        counts[cur_right] = counts.get(cur_right, 0) + 1
        right += 1
        if kinds == len(counts):
            while left < right:
                cur_left = gems[left]
                if counts[cur_left] > 1:
                    counts[cur_left] -= 1
                    left += 1
                elif minimum > right - left:
                    minimum = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break
    return answer


if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))
