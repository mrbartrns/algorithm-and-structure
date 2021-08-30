# 모음 사전
def solution(word):
    ret = set()
    backtrack(0, '', ret)
    ret = list(ret)
    ret.sort()
    return ret.index(word)


def backtrack(idx, word, ret):
    if idx == 5:
        ret.add(word)
        return

    for c in ('', 'A', 'E', 'I', 'O', 'U'):
        backtrack(idx + 1, word + c, ret)


if __name__ == '__main__':
    word = "EIO"
    print(solution(word))
