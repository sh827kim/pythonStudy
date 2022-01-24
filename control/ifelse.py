weather = input("how's the weather? ")

if weather == "rainy" or "snowy":
    print("get your umbrella")
elif weather == "dusty" :
    print("get your mask")
else: 
    print("nothing to need to go outside")

temp = int(input("The temperature is "))
if 30 <= temp:
    print("Too hot to go outside... Stay inside Please..")
elif 10<= temp and temp < 30:
    print("good temp")
elif 0 <= temp < 10:
    print("Get your coat")
else : 
    print("It's cold outside. Don't go.")