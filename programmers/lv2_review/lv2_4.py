# 주식가격
# 스택 큐를 사용하여 문제 해결하는 방법?
def solution(prices):
    res = [0] * len(prices)
    for i in range(len(prices)):
        idx = len(prices) - 1
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                idx = j
                break
        res[i] = idx - i
    return res


a = [1, 2, 3, 2, 3]
print(solution(a))