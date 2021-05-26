# # 파일입출력
# 파일 쓰기
# score_file = open("score.txt", "w", encoding = "utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# # 파일 수정
# score_file = open("score.txt", "a", encoding = "utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 읽기
# score_file = open("score.txt", "r", encoding = "utf8")
# # print(score_file.read())
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()



# # pickle
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":"30", "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# # with
import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있다")

# with open("study.txt", "r", encoding = "utf8") as study_file:
#     print(study_file.read())

# Quiz 8
# 매주 1회 보고서 작성, 1주차 부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
# 1번
# for i in range(1, 51):
#     report = open("{}주차.txt".format(i), "w", encoding="utf8")
#     report.write("""- {}주차 주간보고 -
#     부서 :
#     이름 :
#     업무 요약 : """.format(i))
#     report.close()
# # 2번
# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report
#         report.write("- {}주차 주간보고 -\n".format(i))
#         report.write("부서 : \n")
#         report.write("이름 : \n")
#         report.write("업무 요약 : ")

# # 클래스
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

    def attack(self, name, location, damage):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 10)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)