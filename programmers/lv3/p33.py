# 스타 수열
def solution(a):
    counts = [0] * (len(a) + 1)
    result = 0
    s = set()
    for i in range(len(a)):
        counts[a[i]] += 1
        s.add(a[i])

    for number in s:
        if result >= counts[number]:
            continue

        answer = 0
        left, right = 0, 1

        while left < len(a) and right < len(a):
            if a[left] != a[right] and (a[left] == number or a[right] == number):
                answer += 1
                left = right + 1
                right = left + 1
            else:
                left += 1
                right += 1

        result = max(result, answer)

    return result * 2


if __name__ == "__main__":
    a = [0, 3, 3, 0, 7, 2, 0, 2, 2, 0]
    print(solution(a))
