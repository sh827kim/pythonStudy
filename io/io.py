print("Python", "Java", sep=",")
print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", sep=",", end="? ")
print("More Useful Lang is?")

scores = {"Math":100, "Eng":80, "Coding":95}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

import sys
from this import d

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)


for num in range(1, 21):
    print("Waiting Number : " + str(num).zfill(3))


answer = input("Write any value : ")
print("your answer is :", answer)

# 빈 자리 빈공간으로 두고 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 땐 +, 음수일땐 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마
print("{0:,}".format(100000000000))

# 3자리마다 콤마,부호
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리마다 콤마, 부호, 자릿수 확보, 빈자리는 ^ 로 채우기
print("{0:^<+30,}".format(-100000000000))

# 소수점 출력 
print("{0:f}".format(5/3))
print("{0:.3f}".format(5/3))