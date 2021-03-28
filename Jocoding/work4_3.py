'''
#1
def is_odd(a):
    if a%2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
is_odd(3)


#2
def avg(*args):
    sum = 0
    for i in args:
        sum = sum + i
    average = sum/len(args)
    return average
print(avg(2,3,4,5,6,7))


#3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % (input1 + input2))


#4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))


#5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

with open("test.txt", 'w') as f1:
    f1.write("Life is too short")
with open("test.txt", 'r') as f2:
    print(f2.read())


#6
f1 = open("test.txt", 'w')
for i in range(1,10):
    f1.write("%d번째 줄입니다.\n" % i)
f1.close()

f2 = open("test.txt", 'a')
for i in range(10,20):
    f2.write("%d번째 줄입니다.\n" % i)
f2.close()
'''

#7
f1 = open("test.txt", 'w')
f1.write("Life is too short\nyou need java")
f1.close()

f2 = open("test.txt", "r")
body = f2.read()
f2.close()

body = body.replace("java","python")

f3 = open("test.txt", "w")
f3.write(body)
f3.close()