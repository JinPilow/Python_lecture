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
'''
# Quiz 4
# 20명 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰 수령하게하는 프로그램 작성(중복 불가)

from random import *

applicants = list(range(1, 21))
shuffle(applicants)
chicken = randint(1, 20)
applicants.remove(chicken)

coffee = []
i = 0
while len(coffee) < 3:
    b = randint(1, 20)
    if b in applicants:
        applicants.remove(b)
        coffee.append(b)
        coffee.sort()
    i += 1

print("""** 당첨자 발표 **
치킨 당첨자 : {}
커피 당첨자 : {}
** 축하합니다 **""".format(chicken, coffee))
'''
'''
# Quiz 5
# 당신은 Cocoa 서비스를 이용하는 택시기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수
# 조건2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭

from random import *

count = 0
for i in range(50):
    client = randrange(5, 51)
    if 5 <= client <= 15:
        count = count + 1
        print("[O] {}번째 손님 (소요시간 : {}분)".format(i+1, client))
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(i+1, client))

print("총 탑승 승객 : {} 분".format(count))
'''
'''
# Quiz 6
# 표준 체중을 구하는 프로그램 작성
# <성별에 따른 공식>
# 남성 : 키(m) x 키(m) x 22
# 여성 : 키(m) x 키(m) x 21

def std_weight(height, gender):
    if gender == "남":
        return round(height/100*height/100*22,2)
    elif gender == "여":
        return round(height/100*height/100*21,2)
    else:
        quit()

height = float(input("키를 입력하시오: "))
gender = input("성별을 입력하시오: (예시: 남, 여)")

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight(height, gender)))
'''

# Quiz 7
# import sys
# print("python", "Java", file = sys.stderr)
# print("python", "Java", file = sys.stdout)

# # 왼쪽정렬, 오른쪽 정렬
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#
# # 0 채우기 zfill
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))
#
# # input
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 {} 입니다".format(answer))

# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# # 왼쪽 정렬하고, 빈칸은 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마 찍어주기
# print("{0:,}".format(100000000))
# # 3자리 마다 콤마 찍어주기, 부호 추가
# print("{0:+,}".format(100000000))
# # 3자리 마다 콤마 찍어주기, 부호 추가, 자릿수 확보, 빈 공간은 ^로 채움
# print("{0:^<+30,}".format(100000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수까지만 표시
# print("{0:.3f}".format(5/3))
