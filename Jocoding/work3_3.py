'''
#1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")


#2
i = 1
b = 0
while i < 1000:
    if i%3 == 0"
        b = b + i
    i += 1
print(b)


#3
i = 0
while i <= 5:
    print("*"*i)
    i += 1


#4
for i in range(1,101):
    print(i)


#5
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0

def avg(sum, n):
    average = sum/n
    return average
for i in score:
    sum = sum + i

print(avg(sum, len(score)))
'''

#6
number = [1, 2, 3, 4, 5]
result = [2*i for i in number if i%2 == 1]
print(result)