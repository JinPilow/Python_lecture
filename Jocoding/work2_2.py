'''
#튜플
t1 = (1, 2, 'a', 'b') #튜플은 삽입, 삭제, 교체 모두 불가
t2 = (3, 4)
print(t1.index(2))
print(t1+t2)
print(t1*3)

#딕셔너리
dic = {'name':'Eric', 'age':'15'}
print(dic)
print(dic['name']) # 값이 없을 때 에러
print(dic.get(0)) # 값이 없을 때 None 반환
print(dic.get(2,'없음')) # 값이 없으면 '없음' 반환

a = {1:'a'}
a['name'] = '익명'
print(a)
del a['name']
print(a)

b = {1:'변진욱', 2:'주종문', 3:'파이썬'}
print(b.keys())
print(b.values())
print(b.items())
for i in b.values():
    print(i)

b.clear() #모두 지우기


c = {1:'변진욱', 2:'주종문', 3:'파이썬'}
print(4 in c)# 참 거짓 형태로 반환
print(1 in c)# 참 거짓 형태로 반환


#집합 순서 없음
#s1 = set([1,2,3]) 또는
s1 = {1,2,3} #로 정의
print(s1)
s1.add(4) # 하나 추가
print(s1)
s1.update([5,6,7]) #여러개 추가
print(s1)
s1.remove(1) #하나 삭제

l = [1,1,2,2,2,3,3,4]
Newlist = list(set(l))
print(Newlist) #중복제거

s2 = set('Hello')
print(s2)


s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
#교집합
print(s3 & s4)
print(s3.intersection(s4))
#합집합
print(s3 | s4)
print(s3.union(s4))
#차집합
print(s3-s4)
print(s3.difference(s4))
print(s4.difference(s3))


#bool

a=True
print(a)
print(type(a))

b = "안녕"

if b: #문자나 값이 있으면 참, 없으면 거짓
    print(b)

c=[1,2,3,4]
while c: # 반복문이 돌 때마다 c에서 하나씩 제거하면 결국 c는 False가 됨
    print(c)
    c.pop()

#변수
a = [1,2,3]
b = a
a[1] = 4
print(b) # b는 a의 주소를 참조하고 있으므로 a와 같은 결과가 출력된다.
print(a is b) # a와 b는 같은 주소값을 가지나?

a = [1,2,3]
b = a[:] # a의 주소가 아닌 값만 보내고 싶을 때는 다음과 같이 슬라이싱해서 전달하면 된다.
a[1] = 4
print(b)

#변수 할당 방법
#a, b = 'Python','Java'
#(a,b) = 'Python','Java'
#a,b = ['Python','Java']
#[a,b] = ['Python','Java']
a = b = 'Hello'
print(a)
print(b)
'''

# 일반적인 변수 값 서로 바꾸기
a = 3
b = 5
tmp = b
b = a
a = tmp
# 파이썬 변수 바꾸기
a = 3
b = 5
a, b = b, a
print(a)
print(b)
