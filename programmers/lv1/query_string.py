# [카카오] 숫자 문자열과 영단어
def solution(s):
    s_set = set(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    )
    n_set = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    value_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }
    left = 0
    right = 1
    answer = ""
    while right <= len(s):
        if s[left:right] in n_set:
            answer += s[left:right]
            left += 1
            right += 1
        elif s[left:right] in s_set:
            answer += value_dict[s[left:right]]
            left = right
            right += 1
        else:
            right += 1
    return int(answer)


if __name__ == "__main__":
    s = "123"
    print(solution(s))