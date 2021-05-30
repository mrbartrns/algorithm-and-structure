# 강남역 폭우
def trapping_rain(buildings):
    # 코드를 작성하세요
    res = 0
    for i in range(len(buildings)):
        left = 0
        right = 0
        for j in range(i):
            left = max(left, buildings[j])
        for j in range(i + 1, len(buildings)):
            right = max(right, buildings[j])
        val = min(left, right)
        res += val - buildings[i] if val - buildings[i] > 0 else 0
    return res


if __name__ == "__main__":
    print(trapping_rain([3, 0, 0, 2, 0, 4]))
    print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
