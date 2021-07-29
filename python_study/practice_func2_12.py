# 가변 인자
# def profile(name, age, lang1, lang2, lnag3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lnag5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#","JS")
# profile("김태호", 25, "Kotlin", "Swift")


# 지역 변수와 전역 변수
gun = 10

def checkpoint(soldiers): # 경계근무 나가는 수
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers # 지역변수
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_return(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun # 밖으로 리턴

print("전체 총 :{0}".format(gun))
checkpoint(2) # 2명이 나감
gun = checkpoint_return(gun,2)
print("남은 총: {0}". format(gun))

# quiz 6
''' 표준 체중을 구하는 프로그램을 작성하시오
*표준 체중: 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자: 키(m) * 키(m) * 22
여자: 키(m) * 키(m) * 21

조건 1: 표준 체중은 별도의 함수 내에서 계산
        *함수명: std_weight
        *전달값: 키(height), 성별(gender)
조건 2: 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.'''

def std_weight2(height,gender):
    if gender =="남자":
        weight = round(height * height * 22 / 10000,2) #round(식, 소수점 자릿수)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,weight))
    else:
        weight = round(height * height * 21 / 10000,2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,weight))

std_weight2(175,"남자")
std_weight2(166,"여자")

#강의 답
def std_weight(height,gender): #키는 m단위 (실수), 성별: "남자"/여자
    if gender =="남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))

# 표준 입출력부터 시작