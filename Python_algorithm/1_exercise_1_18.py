'''난수 생성하기'''
# import random

# n = int(input("난수의 개수를 입력하세요:"))

# for _ in range(n):
#     r = random.randint(10,99)
#     print(r, end=' ')
#     if r == 13:
#         print('\n프로그램을 중단합니다.')
#         break
# else:
#     print('\n난수 생성을 종료합니다.')

'''반복문 건너뛰기와 여러 범위 스캔하기'''
# for i in range(1, 13):
#     if i ==8:
#         continue
#     print(i, end=' ')

# print()

'''위 코드를 좀더 효율적으로 활용'''
# for i in list(range(1,8)) + list(range(9,13)):
#     print(i, end=' ')

# print()

'''비교 연산자의 연속 사용방법'''
# print('2자리 양수를 입력하세요')

# while True:
#     no = int(input('값을 입력하세요.:'))
#     if 10 <= no <= 99:
#         break

# print(f'입력받은 양수는 {no} 입니다.')

'''실습 1-21 구구단 출력'''
# print('-' * 27)
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i * j:3}', end='') # i * j를 3자리로 출력
#     print() # 행 변경
# print('-' * 27)
'''
1. 파이썬의 변수는 값을 갖지 않는다
2. 변수는 객체를 참조하는 객체에 연결된 이름에 불과하다
3. 모든 객체는 메모리를 차지하고, 자료형뿐만 아니라 식별번호를 가진다.
4. 파이썬에서 지역변수는 함수가 시작하고 종료함에 따라
객체가 생성되거나 소멸하지 않는다
'''
# n = 1 # 전역 변수(함수 내부 및 외부에서 사용)
# def put_id():
#     x = 1 # 지역 변수(함수 내부에서만 사용)
#     print(f'id(x) = {id(x)}')

# print(f'id(1) = {id(1)}')
# print(f'id(n) = {id(n)}')
# put_id()
