import random


for waiting_no in range(1, 6):
    print("wait number : {0}".format(waiting_no))

coffee_namu = ["ironman", "blackweadow", "captin marble"]

for customer in coffee_namu:
    print("Dear {0}, coffee is ready.".format(customer))


customer = "ironman"
index = 5

while index >=1 :
    print("Dear {0}, coffee is ready. {1} times left".format(customer, index))
    index-=1
    if index == 0 :
        print("coffee thrown..")


# index = 1
# while True:
#     print("Dear {0}, coffee is ready.".format(customer))
#     index+=1

customer = "spark"
person = "Unknown"

# while person!=customer:
#     print("Dear {0}, coffee is ready.".format(customer))
#     person = input("Tell me your nickname please. ")
    

absent = [2, 5]
no_book = [7]

for student in range(1,11): 
    if student in absent:
        continue
    elif student in no_book: 
        print("Today's class is over. {0}, follow me.".format(student))
        break
    print("{0}, Read next page please.".format(student))



#### one line for ####

students = [1, 2, 3, 4, 5]

print(students)
students = [i+100 for i in students]
print(students)

students = ["Kim", "Lee", "Park"]
students = [len(i) for i in students]
print(students)

students = ["Kim", "Lee", "Park"]
students = [i.upper() for i in students]
print(students)

#### Quiz ####

time = []
total = 0

for i in range(0, 50):
    spend = random.randrange(5, 51)
    match = " "
    if 5<= spend <= 15: 
        match = "O"
        total+=1
    print("[{match}] customer {index} : (spent time :{min} min)".format(match=match, index=i, min=spend))

print("Total matched customers : {0} people".format(total))