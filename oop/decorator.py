# decorator review

def print_hello():
    print('hello')


# 데코레이터 형식의 함수
# 어떤 함수를 꾸며서 새로운 함수를 만드는 역할
def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")

    return wrapper


# print_hello = add_print_to(print_hello)
# print_hello()
# add_print_to(print_hello)()

# 또 다른 데코레이터 사용법
@add_print_to
def print_hello():
    print("hello")


print_hello()
