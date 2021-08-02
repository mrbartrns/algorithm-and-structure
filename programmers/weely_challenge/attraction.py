# 부족한 금액 계산하기
def solution(price, money, count):
    s = price * ((count * (count + 1)) // 2)
    return s - money if s > money else 0


if __name__ == "__main__":
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))