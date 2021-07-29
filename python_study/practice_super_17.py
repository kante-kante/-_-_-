# class Unit():
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         # super().__init__() # 다중 상속 시 super를 사용하면 맨 처음 선언했던 클래스만 호출된다.
#         Unit.__init__(self)
#         Flyable.__init__(self)

# 드랍쉽
# dropship = FlyableUnit()

#quiz 8
''' 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
'''
#코드
class House:

    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self. completion_year = completion_year
        
    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)



#나의 답
house1= House("강남","아파트","매매","10억","2010년")
house2= House("마포","오피스텔","전세","5억","2007년")
house3= House("송파","빌라","월세","500/50","2000년")
house1.show_detail()
house2.show_detail()
house3.show_detail()

#강의 답
houses = []
house_1 = House("강남","아파트","매매","10억","2010년")
house_2 = House("마포","오피스텔","전세","5억","2007년")
house_3 = House("송파","빌라","월세","500/50","2000년")
houses.append(house_1)
houses.append(house_2)
houses.append(house_3)

print("총 {0} 대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

''' 예외처리부터 시작'''
