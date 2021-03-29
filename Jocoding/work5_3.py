'''
#1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력


#2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value <= 100:
            self.value += val
        else:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력


#3
print(all([1,2,abs(-3)-3]))
print(chr(ord('a'))=='a')


#4
print(list(filter(lambda a: a>0, [1, -2, 3, -5, 8, -3])))


#5
hex(234)
print(int(hex(234), 16))


#6
print(list(map(lambda a:a*3, [1,2,3,4])))


#7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a)+min(a))


#8
round(17/3, 4)
'''

#9
import sys
numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)
print(result)
