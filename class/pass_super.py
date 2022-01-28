class Unit:
    def __init__(self, name, hp, speed): # __init__ --> 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[ Ground unit moving ]")
        print("{0} : move to {1} direction. [speed : {2}]".format(self.name, location, self.speed))


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

    def damaged(self, damage) :
        print("{0} : {0} damage occured.".format(self.name, damage))
        self.hp -= damage
        print("{0} : remain hp is {1}".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : Destroyed.".format(self.name))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[FlyableUnit Move]")
        self.fly(self.name, location)

#class BuildingUnit(Unit):
#    def __init__(self, name, hp, location):
#        pass # ㅇㅏ무것도 안하고 일단 넘어간다는 의미 

class BuildingUnit(Unit):
   def __init__(self, name, hp, location):
       super().__init__(name, hp)
       self.location = location






supply_depot = BuildingUnit("sp depot", 500, "7")

def game_start():
    print("[Alert] Start new game...")

def game_over():
    pass

game_start()
game_over()