"""
Student객체를 SOLID 원칙에 의거하여 책임을 나누기
하나의 클래스는 하나의 목적만을 위해 존재해야 한다.
"""


class Student:
    def __init__(self, name, id, major):
        self.profile = Profile(name, id, major)
        self.grades = Grades()

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.profile.change_info(new_name, new_id, new_major)

    def print_report_card(self):
        print(self.__str__())

    def __str__(self):
        string = "코드잇 대학 성적표\n\n"
        string += f"학생 이름:{self.profile.name}\n"
        string += f"학생 번호:{self.profile.id}\n"
        string += f"소속 학과:{self.profile.major}\n"
        string += f"평균 학점:{self.grades.get_average()}"
        return string


class Profile:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_info(self, name, id, email):
        self.name = name
        self.id = id
        self.major = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major


class Grades:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)

    def __str__(self):
        return self.get_average()


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.grades.add_grade(3.0)
younghoon.grades.add_grade(3.33)
younghoon.grades.add_grade(3.67)
younghoon.grades.add_grade(4.3)

# print(dir(younghoon))
younghoon.print_report_card()
