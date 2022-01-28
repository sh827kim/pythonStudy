
try: 
    print("dividing calculator")
    nums = []
    nums.append(int(input("First number : ")))
    nums.append(int(input("Second number : ")))
  #  nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error. Wrong value input")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("unknown error")
    print(err)

