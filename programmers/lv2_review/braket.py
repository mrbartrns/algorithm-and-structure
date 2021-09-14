# [카카오] 괄호 변환


def is_correct_braket(u):
    stack = []
    for c in u:
        if stack and stack[-1] == "(" and c == ")":
            stack.pop()
        else:
            stack.append(c)
    return True if not stack else False


def find_balanced_brakets(p):
    u, v = "", ""
    left, right = 0, 0
    i = 0
    while i < len(p):
        u += p[i]
        if p[i] == "(":
            left += 1
        else:
            right += 1
        i += 1
        if left == right:
            break
    v = p[i:]

    return u, v


def solution(p):
    if not p:
        return p
    u, v = find_balanced_brakets(p)
    if is_correct_braket(u):
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


if __name__ == "__main__":
    p = "()))((()"
    print(solution(p))
    # print(find_balanced_brakets(p))
    # print(is_correct_braket(p))