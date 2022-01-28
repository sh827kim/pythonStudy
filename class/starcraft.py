from random import *

class Unit:
    def __init__(self, name, hp, speed): # __init__ --> 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} Unit is created".format(name))
    
    def move(self, location):
        print("{0} : move to {1} direction. [speed : {2}]".format(self.name, location, self.speed))

    def damaged(self, damage) :
        print("{0} : {0} damage occured.".format(self.name, damage))
        self.hp -= damage
        print("{0} : remain hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : Destroyed.".format(self.name))


class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : flying to {1} [speed : {2}]".format(name, location, self.flying_speed))


class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage): # __init__ --> 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : attack enemy , [direction :{1}], [attack:{2}]".format(self.name,location, self.damage))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "marine", 40, 1, 5)
    def steampack(self): 
        if self.hp > 10:
            self.hp-=10
            print("{0} : using steampack (hp 10 decreased) ".format(self.name))
        else:
            print("{0} : Hp is under 10, cannot use steampack.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    
    def __init__(self):
        super().__init__("tank", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False : 
            return
        
        if self.seize_mode == False:
            print("{0} : Seize mode activated".format(self.name))
            self.damage *=2
            self.seize_mode = True
        else :
            print ("{0} : Seize mode deactivated".format(self.name))
            self.damage /=2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__("wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked ==True:
            print("{0} : Clocking mode deactivated.".format(self.name))
            self.clocked = False
        else :
            print("{0} : Clocking mode activated.".format(self.name))
            self.clocked = True

def game_start() :
    print("new game start.")

def game_over() :
    print("player : gg")
    print ("player go out")

game_start()

attack_units = [Marine(), Marine(), Marine(), Tank(), Tank(), Wraith()]

for unit in attack_units:
    unit.move("1")

Tank.seize_developed = True

print("Seize mode developed")

for unit in attack_units:
    if isinstance(unit, Marine) : unit.steampack()
    elif isinstance(unit, Tank) : unit.set_seize_mode()
    elif isinstance(unit, Wraith) : unit.clocking()

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()
