class Unit:
    def __init__(self, name, hp, damage): # __init__ --> 생성자
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} unit created.".format(self.name))
        print("energy {0}, attack {1}".format(self.hp, self.damage))


class AttackUnit: 
    def __init__(self, name, hp, damage): # __init__ --> 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("{0} : attack enemy , [direction :{1}], [attack:{2}]".format(self.name,location, self.damage))

    def damaged(self, damage) :
        print("{0} : {0} damage occured.".format(self.name, damage))
        self.hp -= damage
        print("{0} : remain hp is {1}".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : Destroyed.".format(self.name))

firebat1 = AttackUnit("firebat", 50, 16)

firebat1.attack("5")

firebat1.damaged(25)
firebat1.damaged(25)