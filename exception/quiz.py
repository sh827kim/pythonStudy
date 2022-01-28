# 조건 1 : 1보다 작거나 숫자가 아닌 입력 값이 들어올 때에는 ValueError 로 처리
# 출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨 량은 10마리로 한정
# 치킨 소진 시 사용자 정의 에러 [SoldOutError] 를 발생시키고 프로그램 종료
# 출력메시지 : "재고가 소진되어 더이상 주문을 받지 않습니다."

chicken = 10
waiting =1

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg


while(True):

    try: 
        print("{0} chickens left".format(chicken))
        order = int (input("May I take your order? "))
        if order <= 0 :
            raise ValueError

        if order > chicken:
           print("Insufficient material.")
        else :
            print("[waiting number {0}] {1} chicken order complete.".format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken <=0:
            raise SoldOutError("There's no chicken stocks.")
    except ValueError: 
        print("wrong Value")
    except SoldOutError as err:
        print(err)
        break

    
