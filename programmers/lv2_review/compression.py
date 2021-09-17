# [카카오] 압축

lzw_table = {}


def initialize():
    for i in range(26):
        lzw_table[chr(i + ord("A"))] = i + 1


def solution(msg):
    ret = []
    initialize()
    idx = 27
    left = 0
    right = 1
    while right <= len(msg):
        if msg[left:right] in lzw_table:
            right += 1
        else:
            ret.append(lzw_table[msg[left : right - 1]])
            lzw_table[msg[left:right]] = idx
            left = right - 1
            idx += 1
    ret.append(lzw_table[msg[left : right - 1]])
    return ret


if __name__ == "__main__":
    msg = "ABABABABABABABAB"
    print(solution(msg))