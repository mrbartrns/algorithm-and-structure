# 올바른 괄호
def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and s[i] == ")":
            stack.pop()
        else:
            stack.append(s[i])
    return True if not stack else False


s = "(()("
print(solution(s))