class User:
    # 속성과 행동을 채워넣는다.
    # 인스턴스 메서드 클래스 메서드 정적 메서드
    # instance method
    def say_hello(self):
        print(f"안녕하세요. 저는 {self.name} 입니다.")

    def login(self, email, password):
        if self.email == email and self.password == password:
            print('로그인 성공')
        else:
            print('로그인 실패')

    def check_name(self, name):
        return self.name == name


# User instance 생성
user1 = User()
user1.name = "jackson"
user1.email = "jackson@email.com"
user1.password = "12345"

# 인스턴스 메서드 class.method(instance)
User.say_hello(user1)
user1.say_hello()
user1.login("jackson@email.com", '12345')
