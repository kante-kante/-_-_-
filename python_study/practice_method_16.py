'''메소드, 상속, 다중상속'''
from random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name))
        

#공격 유닛
class AttackUnit(Unit): # Unit을 상속받음
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self, location): # 메소드 앞에는 무조건 self 적는다고 생각
        print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}"\
            .format(self.name, location, self.damage))

    # def damaged(self, damage):
    #     print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
    #     self.hp -= damage
    #     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    #     if self.hp<=0:
    #         print("{0} : 파괴되었습니다.".format(self.name))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    #스팀팩: 일정 시간 동안 이동 및 공격속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp>10:
            self.hp -= 10
            print("{0} : 스팀팩 사용.(hp-10".format(self.name))
        else:
            print("{0} : 체력 부족으로 스팀팩 사용 불가".format(self.name))

#탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시ㅕㅋ, 더 높은 파워로 공격 가능
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 - 시즈모드로 전환
        if self.seize_mode == False:
            print("{0}: 시즈모드로 전환".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드일 떄 - 해제하기
        else:
            print("{0}: 시즈모드를 해제합니다".format(self.name))
            self.damage /=2
            self.seize_mode = False


#메딕: 의무병
# 파이어뱃: 공격 유닛
# firebat1 = AttackUnit("파이어뱃",50, 16)
# firebat1.attack("5시") # self는 따로 적어줄 필요 없음

# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽: 공중 유닛, 공격 불가, 수송기


# 공중 유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0}: {1} 방향으로 날아갑니다. [속도:{2}]"\
            .format(name,location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 상속받은 것 초기화
        Flyable.__init__(self,flying_speed)         # ""   

    def move(self, location): # 메소드 오버라이딩. move 재정의. 지상유닛과 공중유닛 구별을 위함
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)
    
    def clocking(self):
        if self.clocked == True: #클로킹 모드일 때 - 해제하기
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
        else: #클로킹 모드 해제 - 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임 시작")

def game_over():
    print("player: GG")
    print("player 님이 게임에서 퇴장하셨습니다.")


#실제 게임 진행
#게임 시작
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units: # isinstance 해당 객체가 해당 클래스의 객체인지 확인
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20)) #공격은 랜덤으로 받음

#게임 종료
game_over()



#발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

# #벌쳐: 지상 유닛, 기동성 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# #배틀크루저: 공중 유닛, 체력, 공격력 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


'''pass 부터 시작'''
#pass
#건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) #super를 사용하면 self를 사용하지 않는다
#         pass

#서플라이 디폿: 건물, 1개 건물 = 8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass #그냥 넘어간다.

# # game_start()
# # game_over()

