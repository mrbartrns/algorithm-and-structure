# 스타 수열


def solution(a):
    """
    get longest length of subsequence that satisfy star-sequence
    Args:
        a(list): sequence

    Returns(int): longest length of subsequence

    """

    res = 0
    numbers = set()
    counts = [0] * (len(a) + 1)
    for num in a:
        numbers.add(num)
        counts[num] += 1

    for number in numbers:
        if res >= counts[number]:
            continue
        left = 0
        right = 1
        answer = 0
        while left < len(a) and right < len(a):
            if a[left] != a[right] and (a[left] == number or a[right] == number):
                answer += 1
                counts[a[left]] += 1
                counts[a[right]] += 1
                left = right + 1
                right = left + 1
            else:
                left += 1
                right += 1
        res = max(res, answer)
    return res * 2


if __name__ == "__main__":
    a = [1, 2, 1, 3, 4, 1]
    print(solution(a))
"""
import heapq


def solution(a):
    answer = 0
    counts = [0] * (len(a) + 1)
    q = []
    length = len(a)
    for n in a:
        counts[n] += 1
    for i in range(len(counts)):
        if counts[i] > 0:
            heapq.heappush(q, counts[i])
    while q:
        cnt = heapq.heappop(q)
        sub = min(cnt, length - cnt)
        answer = max(answer, sub)
    return answer // 2 * 4
"""
