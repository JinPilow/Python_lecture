'''
def sum(a, b):
    result = a + b
    return result
print(sum(1,2))

def say():
    return 'Hi'
print(say())

def add(a, b): #리턴값이 없는 함수 print(add(3,5)) 했을 시 None이 출력됨
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3, 5)


def sum_many(*args): #arguments
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

def print_kwargs(**kwargs): #keyword arguments
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + k)
print_kwargs(name="조수",b="조")

def sum_and_mul(a,b): #여러개의 값을 튜플 형태로 리턴
    return a+b, a*b, a-b
print(sum_and_mul(1,2))
print(sum_and_mul(1,2)[0])


def say_myself(name,old,man=True): #처음부터 man에 True라는 값을 설정해 놓을 수 있다.
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살 입니다."% old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("부르릉", 27) #세번째 값을 False로 넣으면 "여자입니다." 출력
say_myself(old=27, name="삐뽀", man=False) #값을 넣는 순서가 바뀌어도 맵핑을 직접 해주면 ok


a = 1
def vartest(a): # 함수안의 변수는 지역변수라 함수 밖에 영향을 주지 못한다. Return을 해주거나 Global(전역변수) 사용
    a += 1
vartest(a)
print(a)


#함수 새롭게 표현
#def add(a,b):
#    return a+b

add = lambda a, b: a+b
print(add(1,2))


myList = [lambda a, b: a+b, lambda a, b: a*b] #리스트 안에 def는 못쓰지만 lambda는 가능
print(myList[0](1,3))
print(myList[1](2,4))
'''
