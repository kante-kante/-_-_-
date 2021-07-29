'''자료구조와 배열'''
# 학생 5명의 시험 점수를 입력받아 합계와 평균 구하기

# print('학생 그룹 점수의 평균과 합을 구합니다')

# score1 = int(input('1번 학생의 수를 입력하세요: '))
# score2 = int(input('2번 학생의 수를 입력하세요: '))
# score3 = int(input('3번 학생의 수를 입력하세요: '))
# score4 = int(input('4번 학생의 수를 입력하세요: '))
# score5 = int(input('5번 학생의 수를 입력하세요: '))

# total = 0
# total += score1
# total += score2
# total += score3
# total += score4
# total += score5

# print(f'합계는 {total} 점입니다.')
# print(f'평균은 {total/5}점입니다.')
'''
list에서 원소값을 정하기 않는 리스트는 NONE을 사용 ex) list = [NONE] * 5
tuple의 원소개 1개인 경우 원소 뒤에 반드시 쉼표를 입력해야 한다.
쉼표가 없으면 단순 변수로 인식. 튜플은 ()로 묶어줄 필요는 없다.
'''
# x = [1,2,3]
# a,b,c = x
# print(a,b,c)

# y = [11,22,33,44,55,66,77]
# print(y[2])
# print(y[-3])
# y[-4] = 3.14
# print(y)

# s = [11,22,33,44,55,66,77]
# print(s[0:6])
# print(s[0:7:2])
# print(s[-4:-2])
''' 파이썬에서는 = 가 연산자로 사용되지 않는다.
a=b=1 -> 자바에서는 가능
a=b=1 -> 파이썬에서는 불가능. x=17 등도 마찬가지'''

# 여러 변수에 여러 값을 한꺼번에 대입하기
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# a,b = a+3, b+2
# print(a)
# print(b)

# #누적 대입
# n = 12
# print(id(n))
# n += 1
# print(id(n))

#파이썬 대입기호 차이점 확인
# x = 0
# print(type(x+17))
# print(type(x = 17)) # error. =는 파이썬에서 연산자 취급하지 않음

'''자료구조. 리스트와 튜플'''
# len() 함수를 이용하여 배열의 원소 수 구하기
# x = [15, 64, 3, 3.14, [32,55], 'ABC']
# print(len(x)) # 6

#배열의 최댓값, 최솟값
# x = [10, 35, 7, 38, 42, 29]
# print(min(x)) # 배열의 최솟값
# print(max(x)) # 배열의 최댓값
''' 배열은 조건식을 활용하여 빈 여부 확인 및 비교 연산자로 배열의 대소파악 가능'''
'''
두 객체의 값이 같은지 비교: ==
두 객체의 식별 번호가 같은지 비교: is
'''
# # 내포 표기 생성
# numbers = [1, 2, 3, 4, 5]
# twise = [num * 2 for num in numbers if num % 2 == 1]
# print(twise)

# # 배열 원소를 하나씩 차례로 주목하여 살펴보는 Scan.
# a = [22, 57, 11 ,91 ,32]
# def max_of(a):
#     maximum = a[0]
#     for i in range(1, len(a)): # 하나씩 증가하며 최대값 비교
#         if a[i] > maximum: # 배열의 값이 maximum 보다 크면
#             maximum = a[i] # maximum 에 a[i] 대입
#     print(maximum)
# max_of(a)

''' 배열 원소의 최댓값 출력'''
# from typing import Any, Sequence

# def max_of(a: Sequence) -> Any:
#     # 시퀀스형 a 원소의 최대값 반환
#     maximum = a[0]
#     for i in range(1, len(a)):
#         if a[i] > maximum:
#             maximum = a[i]
#     return maximum

# if __name__ == '__main__':
#     print('배열의 최댓값을 구합니다.')
#     num = int(input('원소 수를 입력하세요'))
#     x = [None] * num # 원소 수가 num 인 리스트 생성

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
#     print(f'최댓값은 {max_of(x)}입니다.')