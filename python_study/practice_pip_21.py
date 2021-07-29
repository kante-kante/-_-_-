# '''pip(pypi 사이트 참조)'''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language)

# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 외장 함수
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py"))# 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder,"폴더를 생성하였습니다.")

# print(os.listdir())

# time: 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%M-%d %H:%M:%S"))

# import datetime
# # print("오늘 날짜는 ",datetime.date.today())

# today = datetime.date.today()
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후

'''Quiz 10
프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
조건: 모듈 파일명은 byme.py로 작성
(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
'''
import byme
byme.sign()
