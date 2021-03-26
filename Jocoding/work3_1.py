'''
##if문
#if 뒤 bool 자료형이 와야함
money = True
if money:
    print("택시")
else:
    print("도보")

a = 1
b = 3
if a < b:
    print("Yes")
else:
    print("No")

bills = 30000
if bills >= 50000:
    print("지불 불가")
else:
    print("지불 가능")

if True | False: # if True or False도 가능
    print("Yup")
else:
    print("Nope")

#if True & False: #if True and False도 가능
#if not True:

if 1 in [1,2,3]:
    print("Yeah")
else:
    print("Nah")

#if 1 not in [1,2,3]: in의 반대

## if~elif~else문

pocket = ['paper', 'cellphone']
card = False
a = True
if 'money' in pocket:
    pass
elif card:
    print("택시를 타고가라")
elif a:
    print("aa")
else:
    print("걸어가라")
'''
#조건부 표현식
score = 70
message = "success" if score >= 60 else "failure"
print(message)
