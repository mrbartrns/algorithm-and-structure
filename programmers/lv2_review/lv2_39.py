# N개의 최소공배수


def solution(arr):
    ans = arr[0]
    for i in range(len(arr)):
        ans = arr[i] * ans // get_gcd(arr[i], ans)
    return ans


def get_gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    return get_gcd(b, a % b)


arr = [2, 6, 8, 14]
print(solution(arr))