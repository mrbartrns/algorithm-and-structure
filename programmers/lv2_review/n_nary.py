# [카카오] n진수
def divide(number, n):
    if number == 0:
        return "0"
    string = ""
    while number > 0:
        left = number % n
        if left >= 10:
            string = chr(ord("A") + left - 10) + string
        else:
            string = str(number % n) + string
        number //= n
    return string


def solution(n, t, m, p):
    number = 0
    string = ""
    while len(string) <= t * m:
        string += divide(number, n)
        number += 1
    answer = ""
    for i in range(len(string)):
        if i == t:
            break
        answer += string[i * m + p - 1]
    return answer


if __name__ == "__main__":
    n = 16
    t = 16
    m = 2
    p = 2
    print(solution(n, t, m, p))