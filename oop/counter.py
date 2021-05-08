"""
시, 분, 초는 각각 자기의 값을 속성으로 갖는다.
시, 분, 초 모두 최댓값이 존재한다. (시는 23, 분, 초는 59)
"""


class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.value = 0

    def set(self, new_value):
        if 0 <= new_value < self.limit:
            self.value = new_value
        else:
            self.value = 0

    def tick(self):
        self.value += 1
        if self.value == self.limit:
            self.value = 0
            return True
        return False

    def __str__(self):
        return str(self.value).zfill(2)


if __name__ == "__main__":
    # 최대 30까지 셀 수 있는 카운터 인스턴스 생성
    counter = Counter(30)

    # 0부터 5까지 센다
    print("1부터 5까지 카운트하기")
    for i in range(5):
        counter.tick()
        print(counter)

    # 타이머 값을 0으로 바꾼다
    print("카운터 값 0으로 설정하기")
    counter.set(0)
    print(counter)

    # 카운터 값 27로 설정
    print("카운터 값 27로 설정하기")
    counter.set(27)
    print(counter)

    # 카운터 값이 30이 되면 0으로 바뀌는지 확인
    print("카운터 값이 30이 되면 0으로 바뀝니다")
    for i in range(5):
        counter.tick()
        print(counter)
