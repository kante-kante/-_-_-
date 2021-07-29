# 배열 원소의 최댓값을 구해서 출력하기(원솟값 입력받기)
from max import max_of # max.py의 max_of 함수 가져오기

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}] 값을 입력하세요.: ')
    if s =='End' or s == 'end':
        break
    x.append(int(s)) # 배열의 맨 끝에 추가
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.') # max.py의 11번째 줄 if문은 실행 x
# __name__이 __main__이 아니기 떄문에
'''배열의 원솟값 난수로 결정하기 부터'''