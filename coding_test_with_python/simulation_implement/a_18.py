# [카카오] 괄호 변환
def solution(w):
    if not w:
        return ""
    left = 0
    right = 0
    idx = 0

    for i in range(len(w)):
        if w[i] == "(":
            left += 1
        elif w[i] == ")":
            right += 1
        if left == right:
            idx = i
            break
    u = w[:idx + 1]
    v = w[idx + 1:]

    if check(u):
        return u + solution(v)

    string = "("
    string += solution(v)
    string += ")"
    for i in range(1, len(u) - 1):
        if u[i] == "(":
            string += ")"
        else:
            string += "("
    return string


def check(u):
    stack = []
    for i in range(len(u)):
        if stack and stack[-1] == "(" and u[i] == ")":
            stack.pop()
        else:
            stack.append(u[i])

    return stack == []


def ret_check(a, b):
    return a == b


if __name__ == "__main__":
    w = "()))((()"
    answer = solution(w)
    print(answer)
    print(ret_check(answer, "()(())()"))
