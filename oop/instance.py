class User:
    """
    SNS의 유저를 나타내는 클래스
    """
    count = 0

    def __init__(self, name: str, email: str, password: str):
        """
        유저의 이름, 이메일, 비밀번호를 입력받고, 이를 저장하는 메서드
        인스턴스가 생성될때마다 class 변수 count를 1 증가시킨다.
        @param name: user's id(nickname)
        @type name: str
        @param email: user's email
        @type email: str
        @param password: user's password
        @type password: str
        """
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def say_hello(self):
        """
        인사말을 출력하는 메서드
        """
        print(f"안녕하세요. 저는 {self.name} 입니다.")

    def login(self, email, password):
        """
        이메일과 비밀번호가 일치하는지 확인하고, 로그인 문구를 출력하는 메서드
        @param email: user's email
        @type email: str
        @param password: user's password
        @tpe email: str
        @return: None
        """
        if self.email == email and self.password == password:
            print('로그인 성공')
        else:
            print('로그인 실패')

    def check_name(self, name):
        """
        주어진 이름과 저장된 유저의 이름이 같은지 체크하는 메서드
        @param name: user's name
        @return: True if self.name == name else False
        @rtype: bool
        """
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
