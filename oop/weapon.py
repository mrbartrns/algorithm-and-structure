"""
캐릭터가 사용할 수 있는 무기를 만드는 클래스
"""
from abc import ABC, abstractmethod


class IWeapon(ABC):
    @abstractmethod
    def use_on(self, other_character):
        pass


class Sword(IWeapon):
    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        other_character.get_damage(self.damage)


class Gun(IWeapon):
    def __init__(self, damage, num_rounds):
        self.damage = damage
        self.num_rounds = num_rounds

    def use_on(self, other_character):
        """총 사용 메소드"""
        if self.num_rounds > 0:
            other_character.get_damage(self.damage)
            self.num_rounds -= 1

        else:
            print("총알이 없어 공격할 수 없습니다.")


class GameCharater:
    def __init__(self, name, hp, weapon: IWeapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self, other_character):
        if self.hp > 0:
            self.weapon.use_on(other_character)
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        self.weapon = new_sword

    def get_damage(self, damage):
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")

    def __str__(self):
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)




