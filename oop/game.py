class GameCharacter:
    # instance 변수 초기화
    def __init__(self, name: str, hp: int, power: int):
        """
        @param name: nickname of character, type str
        @param hp: health point of character, type int
        @param power: type int
        """
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def get_attacked(self, damage):
        if not self.is_alive():
            print(f"{self.name}님은 이미 죽었습니다.")
        else:
            self.hp = self.hp - damage if self.hp >= damage else 0

    def attack(self, other_player):
        other_player.get_attacked(self.power)

    def __str__(self):
        return f"{self.name}님의 hp는 {self.hp}만큼 남았습니다."


# 게임 캐릭터 인스턴스 생성
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)


# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)
