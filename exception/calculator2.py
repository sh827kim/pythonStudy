try:
    print("한자리 숫자 나누기 전용 계산기")
    nums = []
    nums.append(int(input("write your number : ")))
    nums.append(int(input("write your number : ")))

    if nums[0] >= 10 or nums[1] >= 10:
        raise ValueError
    nums.append(int(nums[0]/nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print(" Wrong Value.")

except Exception as err:
    print(err)