from random import randint
from abc import ABC, abstractmethod


class Hero(ABC):
    alive = True
    name = None

    @abstractmethod
    def __init__(self, health, damage, armor=0, attack_range=0, energy=0, live=1):
        self._health = health
        self._damage = damage
        self._live = live
        self._armor = armor
        self._attack_range = attack_range
        self._energy = energy
        self.new_health = self._health

    def __str__(self):
        return "Live = {0._live}\nHealth = {0._health}\nDamage = {0._damage}" \
               "\nArmor = {0._armor}\nAttack_range = {0._attack_range}" \
            "\nEnergy = {0._energy}".format(self)

    def classic_attack(self, enemy):
        if not enemy.dodge():
            enemy._health -= self.damage
            self._energy += 5
            if not enemy.live_checker():
                self._energy += 15
                print(f"{enemy.name} was dead")
        else:
            print(f"{enemy.name} dodged")

    @staticmethod
    def dodge():
        percent = randint(1, 5)
        if percent == 6:
            return True
        return False

    def live_checker(self):
        if self._health == 0:
            self._live -= 1
            if self._live == 0:
                return False
            else:
                self._health = self.new_health
        return True

    def rest(self):
        self._health += randint(4, 12)
        self._energy += 10

    def super_attack(self):

        if self.energy >= 100:
            return "Super must be used"
        return False

    @property
    def live(self):
        return self._live

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage

    @property
    def armor(self):
        return self._armor

    @property
    def attack_range(self):
        return self._attack_range

    @property
    def energy(self):
        return self._energy


class Wizard(Hero):
    name = "Wizard"

    def __init__(self, health, damage, attack_range):
        super().__init__(health, damage)
        self._attack_range = attack_range


class Soldier(Hero):
    name = "Soldier"

    def __init__(self, health, damage, armor):
        super().__init__(health, damage)
        self._armor = armor


class Archer(Hero):
    name = "Archer"

    def __init__(self, health, damage, attack_range):
        super().__init__(health, damage)
        self._attack_range = attack_range


class Knight(Hero):
    name = 'Knight'

    def __init__(self, health, damage, armor, live):
        super().__init__(health, damage, armor)
        self._live = live

    @property
    def live(self):
        return self._live


soldier = Soldier(100, 10, 5)
wizard = Wizard(100, 10, 5)
knight = Knight(100, 10, 5, 2)
archer = Archer(100, 10, 5)

print('*' * 40)
print(soldier)
print('*' * 40)
print(wizard)
print('*' * 40)
print(knight)
print('*' * 40)
print(archer)
print('*' * 40)
