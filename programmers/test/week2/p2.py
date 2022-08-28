def solution(a, b):
    return sum(list(map(lambda x, y: x * y, a, b)))


a = [-1, 0, 1]
b = [1, 0, -1]
print(solution(a, b))