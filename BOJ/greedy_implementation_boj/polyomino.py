# BOJ 1343
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(string):
    ret = []
    arr = list(filter(lambda x: not not x, string.split(".")))
    points = list(filter(lambda x: not not x, string.split("X")))
    for i in range(len(arr)):
        if len(arr[i]) % 2 > 0:
            return -1
    words = get_word(arr)
    if string[0] == ".":
        for i in range(len(points)):
            ret.append(points[i])
            if i < len(words):
                ret.append(words[i])
    else:
        for i in range(len(words)):
            ret.append(words[i])
            if i < len(points):
                ret.append(points[i])
    return "".join(ret)


def get_word(arr):
    ret = []
    for i in range(len(arr)):
        a = len(arr[i]) // 4
        b = len(arr[i]) % 4
        ret.append(a * 'AAAA' + b * 'B')
    return ret


string = si().strip()
print(solve(string))
