# python = "Python is Amazing"
# print(python.lower()) # 소문자로 변환
# print(python.upper()) # 대문자로 변환
# print(python[0].isupper()) # 0번째 문자를 대문자로 변환
# print(len(python)) # 문자의 길이 반환
# print(python.replace("Python","Java")) #앞 단어를 잘라 뒷 단어로 변환

# index= python.index("n") #"n"이 위치한 자릿수를 반환
# print(index)
# index = python.index("n",index+1) #처음 index를 찾은 위치에서 +1부터 n을 다시 찾음
# print(index)

# print(python.find("Java")) #원하는 값이 없을 경우 -1 반환. find와 변수를 이용해서 찾을 때의 차이점
# #print(python.index("Java"))
# print("hi")
# print(python.count("n"))

#문자열 포맷
print("나는 %d살입니다." % 20) # %d는 정수값
print("나는 %s를 좋아해요." % "파이썬") # %s는 스트링반환
print("Apple은 %c로 시작해요." % "A") # %c는 한 글자 반환
print("나는 %s색과 %s색을 좋아해요" %("파랑","빨간"))

#방법2
print("나는 {}살입니다.".format(20)) #{} 속에 집어넣는 format
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))# 순서 인식
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))# 순서 바꿔도 인식

#방법3    
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

#방법4(version 3.6 이상~)
age = 20
color= "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #f로 시작
