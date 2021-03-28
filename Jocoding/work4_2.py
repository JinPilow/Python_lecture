'''
#입력
a = input()
print(a)

number = input("숫자를 입력하시오: ")
print(number)


#출력
print("life" "is" "too short") #lifeistoo short
print("life", "is", "too short") #life is too short

for i in range(10):
    print(i, end=' ') #한 줄에 모아서 출력
for j in range(10):
    print(j, end='hi')
'''
'''
#파일 생성
f = open("새파일.txt", 'w') # w/쓰기모드 r/읽기모드 a/추가모드
f.close()


f = open("새파일.txt", 'w', encoding="UTF-8") #encoding="UTF-8"이라고 쓰면 한글이 안깨지게 출력 가능
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()


#읽기
g = open("새파일.txt", 'r', encoding="UTF-8")
while True:
    line = g.readline() # 어떤 파일을 한 줄씩 읽어오는 함수
    if not line: break
    print(line)
g.close()


g = open("새파일.txt", 'r', encoding="UTF-8")
lines = g.readlines() #리스트 형태로 가져옴
for line in lines:
    print(line.strip("\n"))


f = open("새파일.txt", 'r', encoding="UTF-8")
data = f.read() #한 줄씩 읽어오는 readline/readlines와 달리 read는 한 번에 모두 읽기 가능
print(data)
f.close()


#추가하기
f = open("새파일.txt", 'a', encoding="UTF-8")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

#with문
with open("foo.txt", 'w') as f: #f.close()할 필요가 없이 구문을 빠져나오면 자동으로 종료
    f.write("Life is too short, you need python")