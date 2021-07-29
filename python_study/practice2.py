# print(abs(-5)) # 절대값 반환
# print(pow(4,2)) # 4 ^2 = 16
# print( max(5,12)) # 12
# print(min(5,12)) # 5
# print(round(3.14)) # 3 반올림
# print(round(4.99)) # 5

# from math import *
# print(floor(4.99)) # 내림
# print(cell(3.14)) #올림
# print(sqrt(16)) # 제곱근 구하기

from random import *

# print(random()) # 0.0 < 1.0 미만의 임의 값 생성
# print(random() * 10) # 0.0 < 10.0 미만 임의 값 생성
# print(int(random()*10)) # 0 ~10 미만의 임의 값 생성
# print(int(random() *10)+1) # 1~ 10 이하의 임의 값  생성

# print(int(random() *40)+1)
# print(int(random() *40)+1)
# print(int(random() *40)+1)
# print(int(random() *40)+1)

# print(randrange(1,46)) # 1~45 이하(46 미만)의 임의의 값 생성. 끝값 -1까지

# print(randint(1,40)) # 1 ~ 45 이하의 임의의 값 생성. 처음값과 끝값 포함

day = randrange(4,29)
print("오프라인 스터디 모임 날짜는 매월",str(day),"일로 선정되었습니다.")
# 문자열로 인식시켜주기 위해서 str()로 묶어준다.