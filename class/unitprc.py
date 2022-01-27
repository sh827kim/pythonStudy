class Unit:
    def __init__(self, name, hp, damage): # __init__ --> 생성자
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} unit created.".format(self.name))
        print("energy {0}, attack {1}".format(self.hp, self.damage))

marine1 = Unit("marine", 40, 5)
marine2 = Unit("marine", 40, 5)
marine3 = Unit("marine", 40, 5)
tank = Unit("marine", 150, 35)


wraith1 = Unit("wraith", 80, 5)

print("Unit name : {0}, ATK : {1}".format(wraith1.name, wraith1.damage))


wraith2 = Unit("wraith", 80, 5)

# 멤버변수 확장
wraith2.clocking = True

if wraith2.clocking ==True :
    print("{0} is clocking now.".format(wraith2.name))