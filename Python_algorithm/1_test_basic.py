'''1부터 N까지 정수의 합 구하기(사전 판단 반복 구조)'''
# print("1부터 n까지 정수의 합을 구합니다.")
# n = int(input('n 값을 입력하세요.: '))

# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print(f'1부터 {n}까지 정수의 합은 {sum} 입니다.')
'''i값이 n값을 초과해야 while 문의 반복을 마칠 수 있다.'''

'''1부터 N까지 정수의 합 구하기(for문)'''
# print("1부터 n까지 정수의 합을 구합니다.")
# n = int(input('n 값을 입력하세요.: '))

# sum = 0
# for i in range(1,n+1):
#     sum += i

# print(f'1부터 {n}까지 정수의 합은 {sum} 입니다.')

'''가우스의 덧셈으로 구하기'''
# n = int(input('n 값을 입력하세요.: '))

# sum = n * (n+1) // 2
# print(f'합:{sum}')
# '''//: 몫, %: 나머지'''

'''a부터 b까지 정수의 합 구하기'''
# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b의 값을 입력하세요.: '))

# if a > b:
#     a, b = b, a # a와 b를 오름차순으로 정렬. a와 b의 값을 교환(단일 대입문 사용)

# sum = 0
# for i in range(a, b+1):
#     sum += i

# print(f'{a} 부터 {b}까지 정수의 합은 {sum}입니다.')

'''36 페이지부터 시작'''
# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b의 값을 입력하세요.: '))

# if a> b:
#     a, b = b, a

# sum = 0
# for i in range(a, b + 1):
#     if i < b:
#         print(f'{i} +', end = ' ')
#     else:
#         print(f'{i} = ', end = ' ')
#     sum += i

# print(sum)

'''위에서 사용한 if문 개선코드'''
# print('a부터 b까지 정수의 합을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b의 값을 입력하세요.: '))

# if a > b:
#     a, b = b, a

# sum = 0
# for i in range(a,b):
#     print(f'{i} + ', end = ' ')
#     sum += i

# print(f'{b} = ', end = ' ') # if문에서는 이 값을 위해 필요없는 반복횟수 시행
# sum += b

# print(sum)

'''반복 과정에서 조건 판단(i가 홀수면 -, 짝수면 +)'''
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))

# for i in range(n):
#     if i % 2:
#         print('-', end=' ')
#     else:
#         print('+', end=' ')
# print()

'''위 코드 개선'''
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))

# for i in range(1, n + 1):
#     if i % 2: # 홀수
#         print('+', end=' ')
#     else:
#         print('-', end=' ')

# print()

'''+,- 번갈아 출력'''
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))

# for _ in range(n // 2):
#     print('+-', end='')

# if n % 2:
#     print('+', end = '')

# print()

''' 41페이지 n이 짝수인 경우 출력 '''
# 파이썬에서는 무시하고 싶은 값을 언더스코어로 표시할 수 있다.
# 반복 과정에서 조건 판단하기
# print('*를 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))
# w = int(input('몇 개마다 줄바꿈할까요?: '))

# for i in range(n): # n번 반복
#     print('*', end=' ')
#     if i % w == w - 1: # n번 판단
#         print()         # 줄바꿈

# if n % w:       # 1번 판단
#     print()     # 줄바꿈

'''위 코드 개선'''
# print('*를 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))
# w = int(input('몇 개마다 줄바꿈할까요?: '))

# for _ in range(n // w): # n // w번 반복
#     print('*' * w)

# rest = n % w
# if rest:
#     print('*' * rest)

'''양수만 입력받기'''
# 1 - 8에서 -5를 입력하면 결과값이 이상해지던 문제 수정
# 1-16
# print('1부터 n까지 정수의 합을 구합니다.')

# while True: # 음수값이 입력되면 올바른 값이 나오지 않기 때문에 양수로 한정
#     n = int(input('n값을 입력하세요: '))
#     if n > 0:
#         break  # 무한 루프와 break문

# sum = 0
# i = 1

# for i in range(1, n+1):
#     sum += i
#     i += 1

# print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

''' 보충수업 1-10 for문이 종료된 이후 카운터용 변수 i값 확인'''
'''
while i < =n: # 반복을 종료할 때 i는 n+1
for i in range(시작값, n+1): # 반복을 종료할 때 i는 n'''

# 직사각형 넓이로 변의 길이 구하기. 1-17
# 가로, 세로 길이가 정수이고 넓이가 area인 직사격형에서 변의 길이 나열하기
area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area + 1): # 1부터 사각형의 넓이 계산
    if i * i > area: break
    if area % i: continue
    print(f'{i} x {area // i}')

''' _ 를 카운터용 변수로 사용하면 반환할 값을 생략할 수 있다.'''