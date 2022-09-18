class Pokemon:
    def __init__(self, name, type, hp, attack, defense, special_attack, special_defense, speed):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

class Move:
    def __init__(self, name, type, power, accuracy):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy

class Section:
    def __init__(self, name, obj, winner):
        self.name = name
        self.obj = obj
        self.winner = winner