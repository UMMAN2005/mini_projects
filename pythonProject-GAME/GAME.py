from math import ceil
from random import sample


class Troops(object):
    alive = True

    def __init__(self, name, speed, house_space, hit_points, damage, attack_speed, range_, area):
        self.name = name
        self.speed = speed
        self.house_space = house_space
        self.hit_points = hit_points
        self.damage = damage
        self.attack_speed = attack_speed
        self.range = range_
        self.area = area

    @staticmethod
    def using_range(troop1_, troop2_) -> tuple:
        if troop1_.range >= troop2_.range:
            diff = ceil(troop1_.range - troop2_.range)
            troop2_.hit_points -= (diff * troop1_.damage)
        elif troop2_.range >= troop1_.range:
            diff = ceil(troop2_.range - troop1_.range)
            troop1_.hit_points -= (diff * troop2_.damage)
        return troop1_.hit_points, troop2_.hit_points

    @staticmethod
    def fight(troop1, troop2):
        print("The war begins between {} and {}".format(troop1.name, troop2.name))
        troop1.hit_points, troop2.hit_points = Troops.using_range(troop1, troop2)
        if troop1.area == 'air' and troop2.area == 'land':
            print(f"{troop2.name} was dead")
            print(f"{troop1.name} has {troop1.hit_points} stayed")
        elif troop2.area == 'air' and troop1.area == 'land':
            print(f"{troop1.name} was dead")
            print(f"{troop2.name} has {troop2.hit_points} stayed hit points")
        else:
            while troop1.hit_points > 0 or troop2.hit_points > 0:
                if troop1.hit_points <= 0:
                    print(f"{troop1.name} was dead")
                    print(f"{troop2.name} has {troop2.hit_points} stayed hit points")
                    break
                elif troop2.hit_points <= 0:
                    print(f"{troop2.name} was dead")
                    print(f"{troop1.name} has {troop1.hit_points} stayed hit points")
                    break
                troop1.hit_points -= troop2.damage
                troop2.hit_points -= troop1.damage
            else:
                print(f"{troop1.name} was dead")
                print(f"{troop2.name} was dead")

        return "The war was over"


class Elixir(Troops):
    type = 'elixir'

    def __init__(self, name, speed, house_space, hit_points, damage, attack_speed, range_, area):
        super().__init__(name, speed, house_space, hit_points, damage, attack_speed, range_, area)


class DarkElixir(Troops):
    type = 'dark elixir'

    def __init__(self, name, speed, house_space, hit_points, damage, attack_speed, range_, area):
        super().__init__(name, speed, house_space, hit_points, damage, attack_speed, range_, area)


dragon = Elixir('Dragon', 16, 20, 4900, 370, 1.25, 3, 'air')
electro_dragon = Elixir('Electro-dragon', 13, 30, 5100, 390, 3.5, 3, 'air')
pekka = Elixir('P.E.K.K.A', 16, 25, 7200, 750, 1.8, 0.8, 'land')
dragon_rider = Elixir('Dragon rider', 20, 25, 4700, 400, 1.2, 4, 'air')
electro_titan = Elixir('Electro-titan', 16, 32, 8200, 345, 1.5, 1.25, 'land')
golem = DarkElixir('Golem', 12, 30, 8800, 90, 2.4, 1, 'land')

troop_list = [dragon, dragon_rider, pekka, electro_dragon, electro_titan, golem]
for i in range(3):
    first_troop, second_troop = sample(troop_list, 2)
    print(Troops.fight(first_troop, second_troop))
    troop_list.remove(first_troop)
    troop_list.remove(second_troop)
