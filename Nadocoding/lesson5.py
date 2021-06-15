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
from theater_module import price_soldier as price
price(5)