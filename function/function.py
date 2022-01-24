def open_account():
    print("New Account created")

open_account()

def deposit(balance, money):
    print("Deposited. Balance : {balance} ".format(balance = balance+money))
    return balance + money

def withdraw (balance, money):
    if balance >= money :
        balance -= money
        print("Withdrawal completed. Balance : {balance}".format(balance = balance))
    else :
        print("Insufficient balance. Balance : {balance}".format(balance = balance))
    return balance

def withdraw_night (balance, money):
    commission = 100
    return commission, balance - money - commission



balance = 0
balance = deposit(balance, 10000)
print(balance)


balance = withdraw(balance, 1000)
balance = withdraw(balance, 10000)

commission, balance = withdraw_night(balance, 1000)
print("Commission : {0}, Balance : {1}".format(commission, balance))


#### 기본값 ####

# def profile(name, age, main_lang):
#     print("Name : {0}\tAge : {1}\tMainLang : {2}".format(name, age, main_lang))

# profile("Spark", 30, "Java")
# profile("Kathy", 20, "C++")

def profile(name, age=17, main_lang="Python"):
    print("Name : {0}\tAge : {1}\tMainLang : {2}".format(name, age, main_lang))

profile("Spark")
profile("Kathy")

### 키워드값 ####
def profile(name, age, main_lang):
    print("Name : {0}\tAge : {1}\tMainLang : {2}".format(name, age, main_lang))

profile(name = "Spark", main_lang="Java", age=30)

#### 가변인자 #####

def profile(name, age, *langs):
    print("Name : {0}\tAge : {1}\tMainLang :".format(name, age), end=" ")
    for lang in langs:
        print(lang, end=" ")
    print()

profile("Spark", 30, "Python", "Java", "C", "C++", "Kotlin")
profile("Kate", 30, "C++", "Javascript")


#### 지역변수, 전역변수 ####
gun = 10

def checkpoint(soldiers):
    global gun # 코드 관리가 복잡해지므로 권장하지 않음.
    gun = gun - soldiers
    print("[In func] ramained guns: {0}".format(gun))

print("Total guns: {0}".format(gun))
checkpoint(2)
print("ramained guns: {0}".format(gun))

## 가급적 아래와 같이 리턴값으로 다룰 수 있도록 코드를 작성해야함.
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[In func] ramained guns: {0}".format(gun))
    return gun

print("Total guns: {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("ramained guns: {0}".format(gun))

#### Quiz ####

# woman = h * h * 21, man = h * h * 22

def standard_weight (height, gender) :
    if gender == "F":
        return height*height*21
    else :
        return height*height*22


height = 162
gender = "F"
weight = round(standard_weight(height/100, gender) ,2)

print("Height {0}cm {1}'s st weight : {2}".format(height, gender, weight))