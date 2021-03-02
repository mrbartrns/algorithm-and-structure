# H-index
def solution(citations):
    citations.sort()
    start = 0
    end = len(citations) - 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        h = len(citations) - mid
        if citations[mid] >= h and h >= len(citations) - h:
            answer = h
            end = mid - 1
        else:
            start = mid + 1
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))