import random


class Ship:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def flow(self, flow_direction):
        if flow_direction is True:
            self.speed += random.randrange(50)
        elif flow_direction is None:
            pass
        else:
            self.speed -= random.randrange(50)
        print(f'{self.name}\'s speed at the moment is: {int(self.speed)}km/h')


class Battleship(Ship):

    def __init__(self, name, speed, damage, max_mass):
        Ship.__init__(self, name, speed)
        self.damage = damage
        self.max_mass = max_mass

    def make_stronger(self, quantity_of_guns):
        self.damage += quantity_of_guns * random.randrange(20)
        self.speed -= quantity_of_guns * random.randrange(5)
        self.max_mass -= quantity_of_guns * random.randrange(20)
        print(f'{self.name}\'s damage is: {self.damage}')
        print(f'{self.name}\'s speed at the moment is: {int(self.speed)}km/h')
        if self.max_mass <= 0:
            print('Captain we cannot carry more weapons!')


class Tanker(Ship):

    def __init__(self, name, speed, max_mass):
        Ship.__init__(self, name, speed)
        self.max_mass = max_mass

    def load_in(self, mass):
        self.max_mass -= mass
        if self.max_mass <= 100:
            print('Tanker is fully loaded Captain!')
        self.speed -= mass / 4
        print(f'{self.name}\'s speed at the moment: {int(self.speed)}km/h')


class Submarine(Ship):

    def __init__(self, name, speed, damage):
        Ship.__init__(self, name, speed)
        self.damage = damage


battleship_one = Battleship('Warrior', 300, 800, 300)
battleship_one.make_stronger(10)
battleship_one.flow(True)

tanker_one = Tanker('Georgia', 300, 500)
tanker_one.load_in(500)
tanker_one.flow(None)

submarine_one = Submarine('Sealion', 300, 400)
submarine_one.flow(False)