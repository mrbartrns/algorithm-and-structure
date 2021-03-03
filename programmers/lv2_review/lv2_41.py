# 소수 만들기
def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i + 1 :], r - 1):
                yield [arr[i]] + next


def solution(nums):
    arr = []
    cnt = 0
    for temp in combination(nums, 3):
        arr.append(sum(temp))
    for i in range(len(arr)):
        if is_prime_number(arr[i]):
            cnt += 1
    return cnt


def is_prime_number(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


nums = [1, 2, 7, 6, 4]
print(solution(nums))