"""
클래스 상속
"""


class Employee:
    company_name = "코드잇 버거"
    raise_percentage = 1.03  # 시급 인상률

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    # 클래스 메서드가 아닌 인스턴스 메서드는 self를 이용하여 사용할 수 있다.
    def raise_pay(self):
        self.wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, wage):
        self._wage = wage

    def __str__(self):
        return f"{Employee.company_name} 직원: {self.name}"


class Cashier(Employee):
    raise_percentage = 1.05
    burger_price = 4000

    # 오버라이딩
    def __init__(self, name, wage, number_sold=0):
        """
        겹치는 부분이 존재 -> 더 줄여서 쓸 수 있음
        @param name:
        @param wage:
        @param number_sold:
        """
        # self.name = name
        # self.wage = wage
        # Employee.__init__(self, name, wage)
        super().__init__(name, wage)  # super 함수로 부모클래스의 메소드를 호출이 가능, 매우 중요!
        self.number_sold = number_sold

    def take_order(self, money_received):
        """
        주문과 돈을 받고 거스름돈을 return 한다.
        @param money_received:
        @return:
        """
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    # 오버라이딩
    def __str__(self):
        return f"{Cashier.company_name} 계산대 직원: {self.name}"


class DeliveryMan(Employee):
    pass


if __name__ == "__main__":
    younghoon = Cashier("강영훈", 8900)
    # raise_pay 메서드가 캐셔클래스에 있는지 확인 -> employee 클래스에 있는지 확인 -> 호출
    # 자식 -> 부모순으로 호출되기때문에 오버라이딩이 가능
    younghoon.raise_pay()
    print(younghoon.wage)
    print(younghoon.raise_percentage)  # 1.05
    print(Cashier.mro())
