# 숫자 게임
def solution(a, b):
    a.sort()
    b.sort()
    idx = 0
    answer = 0
    size = len(a)
    visited = [False for _ in range(size)]
    for i in range(size):
        while idx < size:
            if not visited[idx] and b[idx] > a[i]:
                visited[idx] = True
                answer += 1
                break
            idx += 1
    return answer


if __name__ == "__main__":
    a = [2, 2, 2, 2]
    b = [1, 1, 1, 1]
    print(solution(a, b))
