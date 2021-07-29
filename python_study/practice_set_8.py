# # 집합(set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석","박명수"])

# # 교집합(java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python)) # intersection : 교집합

# # 합집합 (java를 할 수 있거나 python를 할 수 있는 개발자)
# print(java | python)
# print(java.union(python)) # union: 합집합

# #차집합(java는 할 수 있지만 python은 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)


# 자료구조의 변경
#커피숍
# menu = {"커피", "우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu , type(menu))

# menu = tuple(menu)
# print(menu , type(menu))

# menu = set(menu)
# print(menu , type(menu))


#quiz
# 1명은 치킨, 3명은 커피쿠폰
# 셔플과 랜덤 활용
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

from random import *
ex_set = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("추첨 인원:",list(ex_set))
shuffle(ex_set)
#print(sample(ex_set,1))

print("치킨 당첨자:", sample(ex_set,1))
shuffle(ex_set)

print("커피 당첨자:",sample(ex_set,3))

#강의 답
users = range(1,21) # 1부터 20의 숫자생성
users = list(users)
shuffle(users)

winners = sample(users,4) # 4명 중에서 1명은 치킨, 3명은 커피
print(winners)

print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))

#if 부터 수업 시작