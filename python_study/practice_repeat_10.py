# absent = [2,5] # 결석
# no_book = [7]
# for student in range(1,11): # 1~10번
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 - 101, 102,103,104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor","Groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor","Groot"]
# students = [i.upper() for i in students]
# print(students)

#quiz 5
''' 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램
조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수
조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야함

(출력문 예제)
[O] 1번째 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간: 50분)
[O] 3번째 손님 ( 소요시간: 5분)
...
[ ] 50번째 손님 (소요시간: 16분)

총 탑승 승객 : 2분
'''
from random import *
# passenger = 0 # 총 탑승 승객 수

# for i in range(1,51):
#     dur = randrange(5,51) # 반복문 내부에서 랜덤 범위 출력하도록 반복
#     if dur >=5 and dur <= 15:
#         print("[O] {0}번째 손님(소요시간: {1}분)".format(i,dur))
#         passenger+=1
#     else:
#         print("[ ] {0}번째 손님(소요시간: {1}분)".format(i,dur))

# print("총 탑승 승객 수: {0}명".format(passenger))


#오답
# if dur >=5 and dur <= 15:
#     print("[O]")
# dur = randrange(5,51) # 이 변수를 반복문 내부에
#ox =""

# while range(1,51) :
#     dur = randrange(5,51)
#     if dur >=5 and dur <15:
#         ox = "O"
#     else:
#         ox=""
#     print("[{0}] {1}번째 손님 (소요시간: {2}분)".format(ox,passenger,dur))


# 강의 답
cnt = 0 # 총 탑승 승객 수
for i in range(1,51): #1 ~ 50이라는 수
    time = randrange(5,51) # 5~50분의 소요시간
    if time >=5 and time <=15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
         print("[O] {0}번째 손님 (소요시간: {1}분)".format(i,time))
         cnt += 1
    else:
         print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, time))

print("총 탑승 승객 수: {0} 분".format(cnt))