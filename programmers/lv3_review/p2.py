# N으로 표현
def solution(n, number):
    if n == number:
        return 1
    dp = [set() for _ in range(8)]
    for i in range(8):
        dp[i].add(int((i + 1) * str(n)))
    for i in range(1, 8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i - j - 1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            return i + 1
    return -1


if __name__ == "__main__":
    n = 2
    number = 11
    print(solution(n, number))
