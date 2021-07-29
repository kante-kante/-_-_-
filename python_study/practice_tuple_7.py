#사전
cabinet = {3:"유재석", 100:"김태호"} # 키값:값
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) #get 메소드를 이용한 값 가져오기
# print(cabinet[5]) # 키값이 없으면 프로그램 종료.
# print(cabinet.get(5)) # 키값이 없으면 none 처리 후 프로그램 계속 실행
# print(cabinet.get(5,"사용 가능")) # 키값이 없으면 사용가능 출력 후 프로그램 계속 실행
# print("hi")

# print(3 in cabinet) # T
# print(5 in cabinet) # F

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

#새 손님
print(cabinet)
cabinet["C-20"]= "조세호" # 새로 키값 및 값 추가. 만약 값이 존재하면 변경
cabinet["A-3"] = "김종국" # 동일 키 값일 시 변경
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# Key 들만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 둘 다 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)



# 튜플 (사전보다 속도가 빠르지만 값 추가 및 변경 불가)
menu = ("돈까스", "치즈 돈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") # 튜플은 값 추가 불가. 고정값

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)