# 최고의 집합
def solution(n, s):
    if s // n < 1:
        return [-1]
    number = s // n
    left = s % n
    arr = [number] * n
    for i in range(n - 1, n - 1 - left, -1):
        arr[i] += 1
    return arr


if __name__ == "__main__":
    n = 2
    s = 1
    print(solution(n, s))
