"""
신용카드를 나타내는 크레딧 카드 클래스
CreditCard 클래스에 들어가는 정보 -> 소유자 이름, 비밀번호, 카드 한도 정보
"""


class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.set_name(name)
        self.set_password(password)
        self.set_payment_limit(payment_limit)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_password(self):
        return "비밀번호는 볼 수 없습니다"

    def set_password(self, password):
        self.__password = password

    def get_payment_limit(self):
        return self.__payment_limit

    def set_payment_limit(self, payment_limit):
        if 0 < payment_limit < CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = payment_limit
        else:
            print("카드 한도는 0 원 ~ 3천만 원 사이로 설정해주세요!")


if __name__ == "__main__":
    card = CreditCard("강영훈", "123", 100000)

    print(card.get_name())
    print(card.get_password())
    print(card.get_payment_limit())

    card.set_name("성태호")
    card.set_password("1234")
    card.set_payment_limit(-10)

    print(card.get_name())
    print(card.get_password())
    print(card.get_payment_limit())
