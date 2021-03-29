'''
#immutable vs mutable
a = 1
def vartest(a):
    a = a+1
vartest(a)
print(a)

b = [1,2,3]
def vartest1(b):
    b.append(4)
vartest1(b)
print(b)


#클래스
class Fourcal(): # 클래스명은 관용적으로 첫글자를 대문자 사용
    def __init__(self,first,second): #클래스를 사용할 시 무조건 실행되는 예약어
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = Fourcal(1,2)
#a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add())

#상속
class MoreFourcal(Fourcal): # 부모클래스의 함수를 그대로 사용 가능
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self): #같은 이름의 함수가 부모클래스 자식클래스에 모두 있을 경우 자식클래스 함수 실행(오버라이딩)
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
b = MoreFourcal(3,5)
print(b.add())
print(b.pow())


class Family():
    lastname = "김" #클래스 변수
    second = 3

#    def __init__(self, first, second): #객체 변수
#        self.first = first
#        self.second = second

Family.lastname = "박" #클래스 변수 자체를 바꿔줌
print(Family.lastname)

a=Family()
b=Family()
print(a.lastname)
print(b.lastname)
'''


