"""
캡슐화
1. 때로는 직접적으로 변수에 접근하여 값을 수정하지 못하도록 하는것이 중요 -> 더블 언더바를 이용하여 접근 제한
2. getter 및 setter 함수를 정의하여 변수의 값을 간접적으로 제어
"""


class Citizen:
    drinking_age = 19

    def __init__(self, name, age, resident_id):
        self.name = name
        # getter와 setter 함수를 정의하여 정의하기
        # self.__age = age
        self.set_age(age)  # 이런식으로 써도 self.__age 정의 가능
        self.__resident_id = resident_id

    def authenticate(self, id_field):
        """
        주민등록번호가 일치하는지 확인하는 함수
        주민등록번호는 민감정보이므로 외부로 노출되어서는 안되며, 쉽게 변경해서도 안된다.
        다만, 필드 값이 주민번호와 일치하는지 확인할 수 있다.
        getter와 setter function을 항상 만들 필요는 없다.
        @param id_field: id number of user
        @type id_field: str
        @return: True if resident id is same with id_field else False
        @rtype: bool
        """
        return self.__resident_id == id_field

    def can_drink(self):
        return self.__age >= Citizen.drinking_age

    # getter function
    def get_age(self):
        return self.__age

    # setter function
    def set_age(self, age):
        """
        age값을 음수로 넣으면 음수가 되므로, set 할때 음수로 받아서는 안된다.
        @param age: age of Citizen
        @type age: int
        @return: None
        """
        if age < 0:
            self.__age = 0
        else:
            self.__age = age

    def __str__(self):
        return f"{self.name} 씨는 {self.__age}살 입니다."


if __name__ == "__main__":
    # double underbar를 붙일 시 외부에서 접근이 불가함
    c1 = Citizen("민병관", 19, "1234567")
    # print(c1.__age)
    print(c1.get_age())
    c1.set_age(25)
    print(c1.get_age())
