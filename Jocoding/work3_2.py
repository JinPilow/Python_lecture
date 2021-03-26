'''
##while문
treehit = 0
while treehit < 10:
    treehit += 1
    print("나무를 %d번 찍었습니다."% treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue #밑에줄 건너띔
    print(a)


##for문
test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

sum = 0
for i in range(1,11):
    sum += i
print(sum)

#구구단1
for i in range(2, 10):
    for j in range(1, 10):
        print("{}*{}={}".format(i,j,i*j))

#구구단2
result = [x*y for x in range(2,10) for y in range(1,10)]


'''
a = [1,2,3,4,5,6,7,8,9,10]
result = [num*3 for num in a if num%2 == 0]

result = []
for num in a:
    if num%2 == 0:
        result.append(num*3)
print(result)