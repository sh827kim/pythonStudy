
pythonStr = "Python is Amazing"

print(pythonStr.lower())
print(pythonStr.upper())
print(pythonStr[0].isupper())
print(len(pythonStr))
print(pythonStr.replace("Python", "Java"))

index = pythonStr.index("n")
print(index)
index = pythonStr.index("n", index + 1)
print(index)
print(pythonStr.find("n"))
print(pythonStr.find("Java"))

print(pythonStr.count("n"))

print("I am %d years old" % 30)
print("I like %s" % "python")
print("Apple spelling starts %c" % "A")


print("I am %s years old" % 30)
print("I like %s" % "python")
print("Apple spelling starts %s" % "A")

print("I like %s and %s" % ("purple", "blue"))
print("I'm {} years old".format(20))
print("I like {1} and {0}".format("purple", "blue"))
print("I'm {age} years old, and my favorite color is {color}".format(age=30, color="blue"))

age = 30
color = "blue"
print(f"I'm {age} years old, and my favorite color is {color}")

print("Never mind. \nI'll find someone like you.")
print("This is the \"WORST\" idea I've ever seen before")
print("\\")
print("Red Apple \rPine")
print("Redd\bApple")
print("Red\tApple")

url = "http://naver.com"
url = url.replace("http://","")
mystr = url[:url.index(".")]
print(mystr[:3] + str(len(mystr)) + str(mystr.count("e")) + "!")