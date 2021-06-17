# # 모듈

# (1)
# import theater_module
#
# theater_module.price(3) # 3명이 영화 보러갈 때 가격
# theater_module.price_morning(4) # 4명이 조조할인 영화 보러갈 때 가격
# theater_module.price_soldier(5) # 5명이 군인할인 영화 보러갈 때 가격

# (2)
# import theater_module as mv
#
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# (3)
# from theater_module import *
#
# price(3)
# price_morning(4)
# price_soldier(5)

# (4)
# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# (5)
# from theater_module import price_soldier as price
# price(5)


# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# print(dir(random)) # 랜덤 모듈 내 어떤 함수를 쓸 수 있는지 표시

lst = [1,2,3]
print(dir(lst)) # 리스트에서 쓸 수 있는 함수 표시

name = "Jim"
print(dir(name))
