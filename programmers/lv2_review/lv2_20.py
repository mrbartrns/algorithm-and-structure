# 구명보트
def solution(people, limit):
    people.sort(key=lambda x: -x)
    left = 0
    right = len(people) - 1
    cnt = 0
    while left <= right:
        if left == right:
            cnt += 1
            break
        else:
            if people[left] + people[right] > limit:
                left += 1
            else:
                left += 1
                right -= 1
            cnt += 1
    return cnt


people = [70, 50, 80]
limit = 100
print(solution(people, limit))
