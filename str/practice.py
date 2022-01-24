# print(abs(-4))
# print(pow(4, 5))
# print(max(5, 12))
# print(min(3, 2))
# print(round(3.14))

from math import *
from random import *

# print(floor(4.99))
# print(ceil(4.3))
# print(sqrt(16))

# print(random())
# print(random() * 10)
# print(int(random()*10))
# print(int(random() * 45) + 1)
# print(randrange(1, 46))
# print(randint(1, 45))

print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4,28)) +" 일로 선정 되었습니다.")

sentence2 = """
난 알고 싶어, 행복을 병속에 담는 법
마법같은 순간 사라지지 않게 간직해 두는 법
사라지지 않게 시간을 되돌릴 순 없나
영원히 깨지 않을 꿈, \
그 속에서 살 수 있게.
"""

print(sentence2)


jumin = "930827-2234578"

print("gender : " + jumin[7])
print("Year : " + jumin[0:2])
print("Month : " + jumin[2:4])
print("Day : " + jumin[4:6])
print("Date : " + jumin[:6])
print("priv : " + jumin[7:])
print("priv : " + jumin[-7:]) # 뒤-7에서부터 끝까지.
