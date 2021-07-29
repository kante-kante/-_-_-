# 패키지: 여러 모듈을 모아놓은 것
# import travel_package.thailand.ThailandPackage # 정의된 함수만을 import 시키는 것은 불가능.
# import travel_package.thailand
# trip_to = travel_package.thailand.ThailandPackage()
# trip_to.detail()

# from travel_package.thailand import ThailandPackage # 정의된 함수만 가져오기 위해서는 from 사용 후 import
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel_package import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
''' __all__부터 시작'''

# from travel_package import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

'''패키지, 모듈 위치'''
import inspect
import random
print(inspect.getfile(random))
# print(inspect.getfile(thailand))