"""
클래스의 다형성
클래스를 이용하여 도형을 나타낼 수 있다.
Rectangle 클래스와 Circle 클래스도 물론 그냥 area와 perimeter라는 메소드를 가질 수는 있습니다.

하지만 Shape 클래스를 상속받았기에 가진 것이 아닌 그냥 메소드를 정의한 것은 상속을 활용한 것이 아닙니다.

상속을 활용한 방법에서는 자식들의 공통점이 될 속성과 행동들을 미리 부모의 클래스에 작성해두고 부모의 속성과 행동을 물려받아 자신만의 속성과 행동들로 변경하기도 합니다.
"""
from abc import ABC, abstractmethod
from math import pi


# Rectangle, Shape은 모두 Shape이라는 공통점을 가진다.
class Shape(ABC):
    """
    추상클래스는 인스턴스 생성이 불가능하다!
    무조건 오버라이딩 하도록 만들기 위해서는? => 추상 클래스 사용
    추상클래스:
    여러 클래스의 공통점들을 추상화 해놓은 클래스
    부모클래스를 추상클래스로 만들 경우, 더 안전한 코드가 된다.
    """

    # 자식 클래스가 무조건 추상화 하도록 만드는 메서드
    @abstractmethod
    def area(self):
        """
        자식 클래스가 오버라이딩 하도록 만듬
        @return:
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        자식 클래스가 오버라이딩 하도록 만듬 (공식이 모두 다르기 때문)
        @return:
        """
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    def __str__(self):
        return f"밑변 {self.width}, 높이 {self.height}인 직사각형"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"반지름 {self.radius}인 원"


class EquilateralTriangle(Shape):
    """
    area, perimeter 메서드가 없지만 shape을 상속받으므로 넓이의 합을 구할 수 있다.
    그러나 오류가 발생 -> 상위 클래스에서 어떠한 값도 반환하지 않으므로

    """

    def __init__(self, side):
        self.side = side


class Cylinder:
    """원통 클래스"""

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


class Paint:
    """그림판 클래스"""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):  # 객체가 클래스에 속하는지 확인하는 함수
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다.")

    def total_area_of_shapes(self):
        """
        shape.area로 각 도형의 넓이를 구한다.
        shape은 circle이 될 수도, rectangle이 될 수도 있다.
        shape이 어떤 도형인지 확인하지 않고 메서드를 호출하지만 에러없이 잘 실행된다.
        다형성의 성질!
        shape에 들어가는 circle 클래스와 rectangle 클래스 모두 area method와 perimeter method를 가지기 때문
        @return:
        """
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """
        shape.parameter로 각 도형의 둘레를 구한다.
        @return:
        """
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str


if __name__ == "__main__":
    rectangle = Rectangle(3, 7)
    circle = Circle(4)

    paint_program = Paint()
    paint_program.add_shape(rectangle)
    paint_program.add_shape(circle)

    print(paint_program.total_area_of_shapes())
    print(paint_program.total_perimeter_of_shapes())
