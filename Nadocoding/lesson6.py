# # 패키지

# import travel.thailand # 패키지만 . 뒤에 추가 가능 모듈 또는 클래스는 직접 import 불가
#
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import * # 패키지의 일부 내용을 비공개 했을 경우 import 불가. __init__ 파일에서 공개처리 해줘야 함
# trip_to = vietnam.VietnamPackage()
# trip_to2 = thailand.ThailandPackage()
# trip_to.detail()
# trip_to2.detail()

import inspect
import random
from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand))