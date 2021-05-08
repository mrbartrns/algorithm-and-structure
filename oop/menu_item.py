class MenuItem:

    # 인스턴스 변수 정의
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 인스턴스 출력 정의
    def __str__(self):
        return f"{self.name} 가격: {self.price}"


