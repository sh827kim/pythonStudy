# marine

name = "marine"
hp = 40
damage = 5

print("{0} unit created.".format(name))
print("energy{0}, attack{1}".format(hp, damage))

# tank

tank_name = "tank"
tank_hp = 150
tank_damage = 35
print("{0} unit created.".format(tank_name))
print("energy{0}, attack{1}".format(tank_hp, tank_damage))

def attack(name, location, damage) :
    print("{0}: attack enemy , [direction :{1}], [attack:{2}]".format(name,location, damage))

attack(name, "1'o Clock", damage)
attack(tank_name, "1'o Clock", damage)