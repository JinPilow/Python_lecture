'''
#구구단
def GuGu(dan):
    gugu =[]
    for i in range(1,10):
        gugu.append(dan*i)
    return gugu

dan = int(input("단을 입력하시오: "))
result = GuGu(dan)
print(result)


#3과 5의 배수 합하기
i = 1
three = 0
five = 0
while True:
    three += 3*i
    five += 5*i
    i += 1
    if 5*i >= 1000:
        five -= 5*i
        while 3*i < 1000:
            three += 3*i
            i += 1
        break
print(three+five)
#-----------------------------------

result = []
for n in range(1,1000):
    if n%3 == 0 or n%5 == 0:
        result.append(n)
    if n%3 == 0 and n%5 == 0:
        result.append(n)
print(sum(result))


#게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지수를 출력하는 프로그램
def GetTotalPage(m,n):
    TotPage =  m//n +1
    print(TotPage)
GetTotalPage(2000,3)


#메모장 만들기
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open("memo".txt, 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open("memo".txt, 'r')
    memo = f.read()
    f.close()
    print(memo)


#탭을 4개의 공백으로 바꾸기
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst,'w')
f.write(space_content)
f.close()
'''

#하위 디렉토리 검색하기 : 파이썬 파일만 출력하기
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass

search("C:/")