# sentence="나는 소년입니다"
# print(sentence)
# sentence2 = "파이썬은 쉽습니다."
# print(sentence2)
# sentence3 = """
# 나는 소년이고
# 파이썬은 쉽습니다
# """
# print(sentence3)

#슬라이싱
jumin = "990120-1234567"

print("성별: "+jumin[7])
print("연: "+jumin[0:2]) #0번째부터 2번째 직전값까지(990의 99까지)
print("월: "+jumin[2:4])
print("일: "+jumin[4:6])
print("생년월일: "+jumin[:6])# 생략하면 생략한곳부터
print("뒷자리: "+jumin[7:])# 끝까지
print("뒷자리(뒤에서부터): "+jumin[-7:])
# 문자열 처리 함수부터 시작