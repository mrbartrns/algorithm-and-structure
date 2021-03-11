# 가장 긴 팰린드롬
import sys

sys.setrecursionlimit(2500)


def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


def solution(s):
    answer = 0
    flag = False
    size = len(s)
    for i in range(size):
        for j in range(len(s)):
            if j + size - i > len(s):
                break
            new = s[j : j + size - i]
            if is_palindrome(new):
                if answer < len(new):
                    answer = len(new)
                    flag = True
                else:
                    return answer
        if flag:
            return answer

    return answer


string = ""
print(solution(string))