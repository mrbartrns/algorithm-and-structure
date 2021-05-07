"""
실습과제
인스턴스를 생성할 때 필요한 정보들이 항상 우리가 원하는 형태로 존재할까? -> No
다향한 형태의 정보에서 필요한 부분을 뽑아내서 인스턴스를 생성할 수 있어야 함
"""


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 클래스메서드를 사용하여 클래스에 필요한 정보를 한번에 채울 수 있다.
    @classmethod
    def from_string(cls, string_params):
        string_list = string_params.split(",")
        # 현재 class에 값을 넣은 인스턴스를 반환한다.
        # 클래스변수에 값을 설정하는것이 아닌 인스턴스 생성시에도 사용이 가능
        # cls는 현재 클래스
        return cls(string_list[0], string_list[1], string_list[2])

    @classmethod
    def from_list(cls, list_params):
        return cls(list_params[0], list_params[1], list_params[2])


younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
