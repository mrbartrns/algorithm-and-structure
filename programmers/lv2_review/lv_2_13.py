# 카카오 괄호변환
def solution(w):
    if not w:
        return ""

    left = right = idx = 0
    for i in range(len(w)):
        if w[i] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            idx = i
            break

    u = w[: idx + 1]
    v = w[idx + 1 :]

    if check(u):
        u = u + solution(v)
        return u
    else:
        string = ""
        string += "("
        string += solution(v)
        string += ")"
        new_ = u[1:-1]
        new_string = ""
        for i in range(len(new_)):
            if new_[i] == "(":
                new_string += ")"
            else:
                new_string += "("
        string += new_string
        return string


def check(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            stack.pop()
    return True if not stack else False


print(solution("()))((()"))