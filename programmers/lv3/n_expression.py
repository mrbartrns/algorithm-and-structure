# N으로 표현
def solution(N, number):
    if N == number:
        return 1

    s = [set() for _ in range(8)]
    for i in range(8):
        s[i].add(int((i + 1) * str(N)))

    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            ans = i + 1
            break
    else:
        ans = -1
    return ans
