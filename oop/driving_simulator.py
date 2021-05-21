"""
상속과 다형성, 추상화 메소드를 이용하여 주행 시뮬레이터 만들기
Point: 어떻게 하면 객체 지향적으로 만들 수 있을 것인가?
요즘은 가상으로 현실과 최대한 비슷한 환경에서 실험할 수 있게 해주는 시뮬레이터 프로그램이 많습니다.
이번 과제에서는 자동차를 마치 실제 도로에서 운전하는 것 같은 체험을 하게 해주는 주행 시뮬레이터를 만들어 볼게요.
본격적으로 주행 시뮬레이터를 만들기 전에 아래의 조건들을 만족하는 프로그램을
 어떻게 객체 지향적으로 작성할 수 있을지 한번 고민해보세요!
 주행 시뮬레이터는:

여러 가지 교통 수단들(일반 자동차, 스포츠카, 자전거 등)을 가질 수 있습니다.
갖고 있는 교통 수단들의 주행을 동시에 시작/정지시킬 수 있습니다.
갖고 있는 교통 수단들의 현재 속도를 문자열 메시지로 볼 수 있습니다.
주행 시뮬레이터가 완성되면 어떻게 사용할 수 있을지 미리 테스트 코드를 보여드리겠습니다.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @property
    @abstractmethod
    def speed(self):
        """
        getter 메소드에 대해서만 추상화 메소드 작성
        @return:
        """
        pass

    def stop(self):
        self.speed = 0


class Bicycle(Vehicle):
    max_speed = 15  # 자전거의 최대 속도

    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        print("자전거 페달 돌리기 시작합니다.")
        self._speed = 5.0

    def __str__(self):
        return f"이 자전거는 현재 {self._speed}km/h로 주행 중입니다."


# 코드를 쓰세요


class NormalCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        print("일반 자동차 시동겁니다.")
        self.speed = self.max_speed / 2

    def __str__(self):
        return f"이 일반 자동차는 현재 {self.speed}km/h로 주행 중입니다."


class SportsCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        print("스포츠카 시동겁니다.")
        self.speed = self.max_speed

    def __str__(self):
        return f"이 스포츠카는 현재 {self.speed}km/h로 주행 중입니다."


class DrivingSimulator:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            print(f"{vehicle}은 교통 수단이 아니기 때문에 추가할 수 없습니다.")

    def start_all_vehicles(self):
        print("모든 교통 수단을 주행 시작시킵니다!\n")
        for vehicle in self.vehicles:
            vehicle.start()

    def stop_all_vehicles(self):
        print("모든 교통 수단을 주행 정지시킵니다!\n")
        for vehicle in self.vehicles:
            vehicle.stop()

    def __str__(self):
        ret = ""
        for vehicle in self.vehicles:
            ret += str(vehicle) + "\n"
        return ret


# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스들
car_1 = NormalCar(0, 100)
car_2 = NormalCar(0, 120)

# 스포츠카 인스턴스들
sports_car_1 = SportsCar(0, 200)
sports_car_2 = SportsCar(0, 190)

# 주행 시뮬레이터 인스턴스
driving_simulator = DrivingSimulator()

# 교통 수단 인스턴스들을 주행 시뮬레이터에 추가한다
driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(car_1)
driving_simulator.add_vehicle(car_2)
driving_simulator.add_vehicle(sports_car_1)
driving_simulator.add_vehicle(sports_car_2)
driving_simulator.add_vehicle(1)

# 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
driving_simulator.start_all_vehicles()
print(driving_simulator)

# 시뮬레이터 내 모든 인스턴스들을 주행 정지시킨다
driving_simulator.stop_all_vehicles()
print(driving_simulator)
