# 이코테 떡 만들기
"""
이진탐색으로 떡볶이 떡 만들기
문제 해결 아이디어:
1) 적절한 높이를 찾을 때까지 이진탐색을 수행하여 높이 H를 반복해서 조정한다.
2) 현재 이 높이로 자르면 만족할 수 있는가? 를 확인한 뒤에 조건의 만족 여부에 따라서
탐색 범위를 좁혀서 해결할 수 있다.
3) 절단기의 높이는 0에서 10억 까지의 정수이므로, 이런 큰 수에 대해서 이진탐색을 떠올려야 한다.
"""
n, m = 4, 6
rice_cakes = [19, 15, 10, 17]
MAX = max(rice_cakes)
MIN = 0


def solve(start, mid, end, length):
    res = 0
    while start <= end:
        cnt = 0
        for i in range(len(rice_cakes)):
            cnt += rice_cakes[i] - mid if rice_cakes[i] - mid > 0 else 0
        if cnt >= length:
            if res < mid:
                res = mid
                start = mid
                mid = (start + end) // 2
            else:
                return res
        else:
            end = mid
            mid = (start + end) // 2
    return res


print(solve(MIN, (MIN + MAX) // 2, MAX, m))