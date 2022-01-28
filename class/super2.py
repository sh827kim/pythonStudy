class Unit:
    def __init__(self):
        print("unit 생성자")

class Flyable: 
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()

## 다중 클래스의 경우 순서상 가장 첫번째 부모에 대해서만 super가 적용된다. 