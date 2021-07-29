# print("Python", "Java",sep=",",end="?") # 각 출력값 사이에 값 삽입:sep, end=문장의 끝 부분에 해당 값 삽입

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

#시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # subject: 키, score: value
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4),sep=":")#ljust,rjust(정수): 정수에 해당하는 칸을 확보하고 왼쪽, 오른쪽 정렬

#은행 대기순번표
# 001, 002, 003
# for num in range(1,21):
#     print("대기번호 :" + str(num).zfill(3)) # zfill: 정수값에 해당하는 만큼 빈공간 확보 및 0으로 채움

# answer = input("아무 값이나 입력하세요:") # 사용자가 입력한 값을 answer에 넣음
# print("입력하신 값은 "+answer + "입니다.") # 사용자가 입력한 값을 받을 때에는 항상 문자열로 받음


#다양한 출력포맥
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) # >: 오른쪽 정렬

# 양수일 때 +로 표시, 음수일 때 -로 표시
print("{0: >+10}".format(500))
print("{0: >10}".format(-500))

# 왼쪽 정렬, 빈칸으로 _로 채움
print("{0:_<10}".format(500)) # <: 왼쪽 정렬

#3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보
# 돈이 많으면 행복하니 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(1000000000))

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정 자리수까지만 표시 (소수점 셋째 자리에서 반올림)
print("{0:.2f}".format(5/3))