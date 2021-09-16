# [카카오] 다트 게임
SQUARE_DICT = {"S": 1, "D": 2, "T": 3}


def calculate(queries):
    ret = []
    for i in range(len(queries[0])):
        current = queries[0][i] ** queries[1][i]
        if queries[2][i] == "#":
            current *= -1
            ret.append(current)
        elif queries[2][i] == "*":
            if ret:
                ret[-1] *= 2
            ret.append(current * 2)
        else:
            ret.append(current)
    return ret


def get_queries(dart_result):
    queries = [[], [], []]
    number = ""
    for c in dart_result:
        if c == "#" or c == "*":
            queries[2][-1] = c
        elif ord(c) < ord("0") or ord(c) > ord("9"):
            queries[0].append(int(number))
            number = ""
            if c in SQUARE_DICT:
                queries[1].append(SQUARE_DICT[c])
                queries[2].append("")
        else:
            number += c
    return queries


def solution(dart_result):
    queries = get_queries(dart_result)
    return sum(calculate(queries))


if __name__ == "__main__":
    dart_result = "1S*2T*3S"
    print(solution(dart_result))