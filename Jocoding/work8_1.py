'''
#1
a = "a:b:c:d"
b = a.split(":")
c = "#".join(b)
print(c)

#2
a = {'A':90, 'B':80}
a.get('C',70)


#3
a = [1,2,3]
a = a + [4,5]

b = [1,2,3]
b.extend([4,5])

print(id(a))
print(id(b))


#4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i >= 50:
        sum = sum + i
print(sum)


#5
n = int(input("숫자를 입력하시오: "))
lst = []
i = 0
while True:
    if i == 0 or i == 1:
        lst.append(i)
    else:
        lst.append(lst[i-1]+lst[i-2])
    if lst[i] <= n:
        pass
    else:
        lst.remove(lst[i])
        break
    i += 1
print(lst)


#6
a = input("숫자를 입력하시오: ")
b = list(map(int, a.split(",")))
total = 0
for i in b:
    total += i
print(total)


#7
n = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
for i in range(1,10):
        print(n*i, end=" ")


#8
f1 = open("abc.txt", 'w')
f1.write("""AAA
BBB
CCC
DDD
EEE""")
f1.close()

f2 = open("abc.txt", 'r')
lines = f2.readlines()
f2.close()
lines.reverse()
print(lines)

f3 = open("abc.txt", 'w')
for line in lines:
    line = line.strip()
    f3.write(line)
    f3.write('\n')
f3.close()


#9
f1 = open("sample.txt", 'w')
f1.write("""70
60
55
75
95
90
80
80
85
100""")
f1.close()

f2 = open("sample.txt", 'r')
lines = f2.readlines()
a=[]
for line in lines:
    line = line.strip()
    a.append(line)
a = list(map(int, a))

total = sum(a)
avg = total/len(a)
print(total, avg)

f3 = open("result.txt", 'w')
f3.write(str(avg))
f3.close()
'''

#10
class Calculator:
    def __init__(self, numlist):
        self.numlist = numlist

    def sum(self):
        result = sum(self.numlist)
        return result

    def avg(self):
        result = sum(self.numlist)/len(self.numlist)
        return result

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())