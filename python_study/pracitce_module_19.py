# # 모듈
# import theater_module
# theater_module.price(3) # 3명이서 영화보러 갔을 때 가격
# theater_module.price_morning(4) # 4명 조조할인 가격
# theater_module.price_soldier(5) # 5명 군인할인 가격

# 모듈명이 길 때 as를 통해 줄여서 사용
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

#전체를 임포트
# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

#특정 함수만 임포트
from theater_module import price, price_morning
price(3)
price_morning(5)
#price_soldier(7)
