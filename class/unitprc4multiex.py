class Unit:
    def __init__(self, name, hp): # __init__ --> 생성자
        self.name = name
        self.hp = hp


class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : flying to {1} [speed : {2}]".format(name, location, self.flying_speed))


class AttackUnit(Unit): 
    def __init__(self, name, hp, damage): # __init__ --> 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : attack enemy , [direction :{1}], [attack:{2}]".format(self.name,location, self.damage))

    def damaged(self, damage) :
        print("{0} : {0} damage occured.".format(self.name, damage))
        self.hp -= damage
        print("{0} : remain hp is {1}".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : Destroyed.".format(self.name))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3")