# 예외처리

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요: ")))
#     nums.append(int(input("두번째 숫자를 입력하세요: ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
# except ValueError:
#     print("에러. 잘못된 값을 입력하셨습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

#사용자 정의 예외처리 - 에러 정의
# class BigNumberError(Exception):
#     pass

# # 한자리 숫자 나누기 전용 계산기
# try:
#     print("한자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >=10 or num2 >= 10:
#         raise BigNumberError("입력값: {0}, {1}".format(num1,num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

#quiz 9
''' 적절한 예외처리 구문을 넣으시오

조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
출력 메시지: "잘못된 값을 입력하였습니다."

조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지: "재고가 소진되어 더이상 주문을 받지 않습니다."
'''
'''#예시코드 및 내 답
class SoldOutError(Exception):
    pass
class OutOfNumber(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 현재만석. 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise OutOfNumber
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -=order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더이상 주문을 받지 않습니다.")
        break # 여기 부분 오답
    except OutOfNumber:
        print("0이나 음수는 입력하실 수 없습니다.")'''

#강의 답
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 현재만석. 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -=order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더이상 주문을 받지 않습니다.")
        break # 오류 위치에서 break를 사용하면 while문 탈출 가능
