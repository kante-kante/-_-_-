# # #탈출문자
# # print("백문이 불여일견 \n백견이 불여일타")
# # print('저는 "kant"입니다.')
# # print("저는 \"kant\"입니다.") # \" \' : 문장 내에서 따옴표

# # \\ : 문장 내에서 \
# print("C:\\python_study>")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple \rPine")

# # \b: 백스페이스
# print("Redd\bApple")

# # \t: 탭
# print("Red\tApple")

#quiz
ex = "http://naver.com"
ex1 = ex[7:ex.index(".")]
print("사이트:",ex1)
print("생성된 사이트:",ex1[0:3] + str(len(ex1))+str(ex1.count("e"))+"!")

#강의 답
url = "http://naver.com"
my_str = url.replace("http://","") #규칙 1
#print(my_str)
my_str = my_str[:my_str.index(".")] # my_str[0:5] = 0~5 직전까지.
#print(my_str)
pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, pwd))