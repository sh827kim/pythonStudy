## 주어진 코드를 활용하여 부동산 프로그램을 만드시오.

## 출력 예제
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House : 
    def __init__ (self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{location} {house_type} {deal_type} {price} {completion_year}" \
            .format(location= self.location, house_type = self.house_type, deal_type = self.deal_type, price = self.price, completion_year = self.completion_year))


gangnam = House("강남", "아파트", "매매", "10억", "2010년")
mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa = House("송파", "빌라", "월세", "500/50", "2000년")

houses = [gangnam, mapo, songpa]

print ("There are 3 houses in my office.")
for house in houses:
    house.show_detail()