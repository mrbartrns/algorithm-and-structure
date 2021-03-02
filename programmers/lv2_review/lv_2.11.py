# 큰 수 만들기 (greedy)
def solution(number, k):
    numbers = list(map(int, list(number)))
    res = []
    cnt = k
    for i in range(len(numbers)):
        while cnt > 0 and res and res[-1] < numbers[i]:
            res.pop()
            cnt -= 1

        res.append(numbers[i])

    while cnt > 0:
        res.pop()
        cnt -= 1

    return "".join(list(map(str, res)))


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))