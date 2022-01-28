class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한자리 숫자 나누기 전용 계산기")
    nums = []
    nums.append(int(input("write your number : ")))
    nums.append(int(input("write your number : ")))

    if nums[0] >= 10 or nums[1] >= 10:
        raise BigNumberError("Write Val {0}, {1}".format(nums[0], nums[1]))
    nums.append(int(nums[0]/nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except BigNumberError as err:
    print("number is too big")
    print(err)
except ValueError:
    print(" Wrong Value.")
except Exception as err:
    print(err)
finally:
    print ("Thank you for using Calculator.")