"""
decorator 사용하는 캡슐화 방법에 대하여 설명
데코레이터를 쓰고 나면 하이라이팅된 부분이 실행
print(instance.age)에서 age getter 메서드가 자동으로 실행됨
데코레이터를 쓰기전, age 인스턴스 변수의 값을 가져오는 용도로 사용되었으나
데코레이터를 쓰면 그 의미가 변함 -> 같은 의미를 갖는 age메서드를 실행하라는 뜻으로 바뀜
instance.age = 30 으로 실행시, 마찬가지로 age.setter 데코레이터 함수가 실행됨 -> value 파라미터로 30이 전달

기존코드를 수정하지 않아도 캡슐화가 가능하다.

객체를 사용할 때에는 최대한 메서드 이용
"""


class Citizen:
    """
    캡슐화를 적용하기 이전의 코드
    """
    drinking_age = 19

    def __init__(self, name, age, resident_id):
        """
        age는 _age에 대한 getter, setter메서드의 이름으로 바뀐다.
        @param name:
        @param age:
        @param resident_id:
        """
        self.name = name
        self.age = age  # property decorator와 이름이 동일해야 함
        self._resident_id = resident_id

    def authenticate(self, id_field):
        return self._resident_id == id_field

    def can_drink(self):
        return self.age >= Citizen.drinking_age

    def __str__(self):
        return f"{self.name}씨는 {self.age}살 입니다."

    @property
    def age(self) -> int:
        """
        _age의 getter 역할을 함
        _age의 getter 메서드 -> get_age와 동일한 메서드
        @return: private self._age
        @rtype: int
        """
        print("나이를 리턴합니다.")
        return self._age

    @age.setter
    def age(self, value):
        """
        getter 메서드의 이름인 age.뒤에 setter를 사용하면, setter 함수를 만들 수 있다.
        _age의 setter 역할을 함 -> set_age와 동일한 메서드
       @param value:
        @return:
        """
        print("나이를 설정합니다.")
        if value < 0:
            self._age = 0
        else:
            self._age = value


if __name__ == "__main__":
    young = Citizen("younghoon kang", 15, "12341234")
    print(young.age)  # 나이를 리턴합니다.\n 15
    young.age = 30  # 나이를 설정합니다.
    print(young.age)  # 나이를 리턴합니다.\n 30
