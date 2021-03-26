'''a= 'life is too short \n but I\'m strong'
b= '\\'

c= """나는 너에 대해서 모르지만
너에게 무슨 일이 일어날지 궁금하다.
    네가 내게 알려줄 용의가 있다면
\t 그곳으로 오라"""
print(a+'\n'+c)

print(a[:7:2])
print(a[-1])
print(a[-4:])
print(a.count('i'))
print(a.find('s'))


days = int(input("얼마?"))
f = int(input("몇개?"))
e = "I eat %d apples so I was satisfied for %d days" % (f, days)
#%d는 정수 %f는 실수 %s는 문자열
print(e)


g = "야 {name}아 뭐하냐".format(name='종문')
print(g)

h = "%10syo" % '바보'
print(h)

i = "%0.4f" % 3.4123485490
print(i)
'''
'''
a =','.join(['a','b','c','d'])
print(a)
b=['a','b','c']
print(b)
c="HI"
print(c.lower())
d=" HI "
print(d.strip())
print(d.replace('H','KA'))

e="a:b:c:d"
print(e.split(":"))
'''
a=['a','b',['c','d']]
print(a[2][1])
del a[0]
a.append('e')
print(a)
a.reverse()
print(a)

b=[1,2,7,5,4]
b.sort()
print(b)
print(b.index(7))
b.insert(0,9)
print(b)
b.remove(5)
print(b)

c=[1,3,5,7,9,11]
print(c.pop(3))
print(c.count(1))
c.extend([2,4])
print(c)