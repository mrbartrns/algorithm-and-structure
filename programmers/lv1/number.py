table = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(s):
    ret = ""
    number = ""
    for c in s:
        if number in table:
            ret += table[number]
            number = ""
        if ord("0") <= ord(c) <= ord("9"):
            ret += c
        else:
            number += c
    if number in table:
        ret += table[number]
    return int(ret)


if __name__ == "__main__":
    s = "2three45sixseven"
    print(solution(s))