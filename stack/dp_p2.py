class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1) if len(self.items) != 0 else None

    def peek(self):
        return self.items[-1] if len(self.items) != 0 else None

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return str(self.items)


def check_bracket(string):
    brackets = Stack()
    pops = ""
    for c in string:
        if c == "{" or c == "(":
            brackets.push(c)
        elif c == "}":
            if brackets.peek() == "{":
                pops = brackets.pop()
            else:
                return 0
        elif c == ")":
            if brackets.peek() == "(":
                pops = brackets.pop()
            else:
                return 0
    return 1 if brackets.is_empty() and pops else 0


print(check_bracket("({(})})"))
print(check_bracket("{((((()))))}"))
# t = int(input())
# for i in range(t):
#     string = input()
#     print(f'#{i + 1} {check_bracket(string)}')
