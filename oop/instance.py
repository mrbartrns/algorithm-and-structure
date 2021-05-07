class User:
    # 속성과 행동을 채워넣는다.
    # 인스턴스 메서드 클래스 메서드 정적 메서드
    # instance method
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def say_hello(self):
        print(f"안녕하세요. 저는 {self.name} 입니다.")

    def login(self, email, password):
        if self.email == email and self.password == password:
            print('로그인 성공')
        else:
            print('로그인 실패')

    def check_name(self, name):
        return self.name == name

    # decorator
    @classmethod
    def number_of_users(cls):  # User == cls
        print("클래스 변수 입니다: {}".format(cls.count))


# User instance 생성
user1 = User("jackson", "1", "2")
user2 = User("jack", "2", "3")
user3 = User("son", "3", "4")

# 클래스 변수
print(User.count)
# 인스턴스변수가 따로 설정되어 있지 않을때 클래스 변수가 줄력됨
# print(user1.count)
# print(user2.count)
# print(user3.count)

User.number_of_users()
user1.number_of_users()

# 인스턴스 메서드 class.method(instance)
# User.say_hello(user1)
# user1.say_hello()
# user1.login("jackson@email.com", '12345')
