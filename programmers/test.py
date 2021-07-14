def solution(a):
    answer = 0
    counts = [0] * len(a)
    if len(a) <= 1:
        return answer
    s = set()
    for i in range(len(a)):
        s.add(a[i])
        counts[a[i]] += 1

    for number in s:
        if counts[number] <= answer:
            continue
        left = 0
        right = 1
        res = 0
        while right < len(a):
            if a[left] != a[right] and (a[left] == number or a[right] == number):
                res += 1
                left = right + 1
                right = left + 1
            else:
                left += 1
                right += 1
        answer = max(res, answer)
    return answer * 2


if __name__ == "__main__":
    a = [5, 2, 3, 3, 5, 3]
    print(solution(a))
