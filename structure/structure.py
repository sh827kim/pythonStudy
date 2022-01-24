#### list ####

subway = [10, 20, 30]
print(subway)

subway = ["clark", "kelly", "jack"]
print(subway.index("clark"))

subway.append("kim")
print(subway)

subway.insert(1, "rick")
print(subway)

subway.pop()
print(subway)

subway.append("rick")
print(subway.count("rick"))

num_list = [2,3,5,4,1]

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

mix_list = ["spark", 10, True]
print(mix_list)

num_list = [2,3,5,4,1]
num_list.extend(mix_list)
print(num_list)

#### dictionary (map) ####
cabinet = {3:"spark", 4:"ich", 100:"rock"}
print(cabinet[3])
print(cabinet.get(100))
print(cabinet.get(5))
print(cabinet.get(5, "not used"))


print(3 in cabinet)
print(5 in cabinet)


cabinet = {"A-3":"Spark", "B-100":"Kasper"}
cabinet["C-20"] = "Genie"
cabinet["A-3"] = "Luna"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)

#### tuple - immutable list.. ####
menu = ("steak", "lobster")
print(menu[0])

#name  = "Spark"
#age = 30
#hobby = "singing"
(name, age, hobby) = ("Spark", 30, "singing")

print(name, age, hobby)


#### set (집합) ####
my_set = {1,2,3,3,3}
print(my_set)

# set 테스트

java = {"King", "Princess", "Emperor"}
python = set(["King", "Queen"])

# 교집합 
print(java & python)
print(java.intersection(python))

# 합집합

print(java | python)
print(java.union(python))

# 차집합 
print(java - python)
print(java.difference(python))

# 
python.add("Princess")
print(python)

java.remove("Emperor")
print(java)


#### switch structure ####

menu = {"Coffee", "Milk", "Juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


#### quiz ####

from random import *

ids = range(1, 21)
ids = list(ids)
shuffle(ids)

chicken_winner = sample(ids, 1)

print("------ winners!! ------")
print("chicken winner : {}".format(chicken_winner[0]))

ids.remove(chicken_winner[0])
shuffle(ids)
print("coffee winner : {}".format(sample(ids, 3)))
print("Congratuations!")