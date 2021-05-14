"""
클래스 상속 연습
"""


class Employee:
    company_name = "코드잇 버거"
    raise_percentage = 1.03
    position = "직원"

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def raise_pay(self):
        self.wage *= self.raise_percentage

    def __str__(self):
        return f"{Employee.company_name} {self.position}: {self.name}"


class DeliveryMan(Employee):
    position = "배달원"

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver(self, address):
        if self.on_standby:
            print(f"{address}로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """
        배달원의 복귀를 처리하는 함수
        @return:
        """
        self.on_standby = True


