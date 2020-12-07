def solve(string):
    stack = []
    for c in string:
        if stack == []:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    return len(stack)


t = int(input())
for i in range(t):
    string = input()
    print(f"#{i + 1} {solve(string)}")
