"""
0 또는 시작값에서 특정 최댓값까지 숫자를 증가시키는 Counter 클래스를 정의했다.
Counter 클래스로 어떻게 시계의 시, 분, 초를 나타낼 수 있을까? -> 먼저 시계라는 객체도 클래스로 정의
시계 프로그램은 다음을 만족해야 함
1. 현재 시각을 설정할 수 있다.
2. 현재 시간을 변경할 수 있다.
3. 현재 시간에 1초씩 더할 수 있다.
"""
from counter import Counter


class Clock:
    HOURS = 24
    MINUTES = 60
    SECONDS = 60

    def __init__(self, hour, minute, second):
        """
        Counter클래스를 이용하여 hour, minute, second를 정의했으므로 인스턴스를 이용하여 직접 값을
        변경하는 것은 허용하지 않는다.
        @param hour: int
        @param minute: int
        @param second: int
        """

        self.hour = Counter(Clock.HOURS)
        self.minute = Counter(Clock.MINUTES)
        self.second = Counter(Clock.SECONDS)
        # Counter 클래스의 set 메서드를 이용하여 값을 설정
        # self.hour.set(hour)
        # self.minute.set(minute)
        # self.second.set(second)
        # set 메서드를 정의한후 init에 사용하면 더 간결하게 표현 가능
        self.set(hour, minute, second)

    def set(self, hour, minute, second):
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)

    def tick(self):
        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}"


if __name__ == "__main__":
    # 초가 60이 넘을 때 분이 늘어나는지 확인하기
    print("시간을 1시 30분 48초로 설정합니다")
    clock = Clock(1, 30, 48)
    print(clock)

    # 13초를 늘린다
    print("13초가 흘렀습니다")
    for i in range(13):
        clock.tick()
    print(clock)

    # 분이 60이 넘을 때 시간이 늘어나는지 확인
    print("시간을 2시 59분 58초로 설정합니다")
    clock.set(2, 59, 58)
    print(clock)

    # 5초를 늘린다
    print("5초가 흘렀습니다")
    for i in range(5):
        clock.tick()
    print(clock)

    # 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
    print("시간을 23시 59분 57초로 설정합니다")
    clock.set(23, 59, 57)
    print(clock)

    # 5초를 늘린다
    print("5초가 흘렀습니다")
    for i in range(5):
        clock.tick()
    print(clock)
