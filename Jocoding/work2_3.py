#1
subject = {'국어':80, '영어': 75, '수학': 55}

add = 0
for i in subject.values():
    add += i

avg = add / len(subject)
print(avg)

#2
if 13%2==1:
    print("홀수")
else:
    print("짝수")

#3
a = "881120-1068234"
b = a.split("-")
print(b[0])
print(b[1])
#print(a.split("-"))

#4
if int(a[7])%2 == 0:
    print("여자")
else:
    print("남자")

#5
c = "a:b:c:d"
print(c.replace(":","#"))

#6
d = [1,3,5,4,2]
d.sort()
d.reverse()
print(d)

#7
e = ['Life','is','too','short']
f = " ".join(e)
print(f)

#8
t1 = (1,2,3)
t2 = (4,)
print(t1+t2)

#10
g = {'A':90, 'B':80, 'C':70}
print(g.pop('B'))

#11
h = [1,1,1,2,2,3,3,3,4,4,5]
i = list(set(h))
print(i)