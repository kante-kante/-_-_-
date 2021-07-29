# score_file= open("score.txt","w",encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기 동작 수행. 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#몇 줄인지 모를때
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


'''피클(pickle)'''
# import pickle
# # profile_file = open("profile.pickle","wb") # b: 바이너리. 피클은 항상 바이너리
# # profile={"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# # profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


'''with'''
# import pickle
# with open("profile_pickle","rb") as profile_file: # 파일을 profile_file로 저장
#     print(pickle.load(profile_file))

# with open("study.txt","w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","r", encoding="utf8") as study_file:
#     print(study_file.read()) # 매번  close할 필요가 없다

#quiz 7
''' 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
- X 주차 주간보고 -
부서: 
이름: 
업무 요약: 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건: 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다."'''

for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약:")