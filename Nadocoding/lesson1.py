'''
# Quiz 1

station = ["사당","신도림","인청공항"]
for i in station:
    print(i + "행 열차가 들어오고 있습니다.")

print(end="\n")

for i in station:
    print("{}행 열차가 들어오고 있습니다.".format(i))

print(end="\n")

for i in range(3):
    print("%s행 열차가 들어오고 있습니다." %(station[i]))
'''
'''
# Quiz 2
# 월 4회 스터디 모임 날짜 무작위로 정하기(모임 4회, 그 중 오프라인 미팅 1회)
from random import *

month = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31,
        '11':30, '12':31}
n = input("달을 입력하시오: ")

meeting_date = []
i = 0
while len(meeting_date) <= 3:
    a = randint(1, month[n])
    if a not in meeting_date:
        meeting_date.append(a)
    i += 1

meeting_date.sort()
offline = sample(meeting_date, 1)

print("{}월 코딩 스터디 모임은".format(n), end=' ')
for i in meeting_date:
    if i == meeting_date[3]:
        print(i, end='')
    else:
        print(i, end=', ')
print("일 입니다.")
print("오프라인 스터디 모임 날짜는 {}월 {}일로 선정되었습니다.".format(n, offline))
'''
'''
# Quiz 3
# 사이트별로 비밀번호를 만들어 주는 프로그램 작성
# 예) http://naver.com
# 규칙 1 : http://부분은 제외 => naver.com
# 규칙 2 : 처음 만나본 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

site = "http://google.com"
index = site.index(".")
site1 = site[7:index]
password = ""
password = password + site1[:3] + str(len(site1)) + str(site1.count("e")) + "!"
print(password)
'''

# Quiz 4
# 20명 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰 수령하게하는 프로그램 작성(중복 불가)

from random import *

applicants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = randint(1, 20)
if a in applicants:
