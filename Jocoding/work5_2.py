
##모듈
'''
import mod1
print(mod1.add(1,2))
#=
from mod1 import add
print(add(1,2))
'''
#import해오는 파일의 경로가 다를 경우
#import sys
#sys.path.append("C:\git\Python")
#import mod1
#print(mod1.add(3,4))

##패키지 (모듈 여러 개를 모아놓은 것)
'''
game/
    __init__.py #패키지에 관한 내용을 저장한 관용 제목
    sound/
        __init__.py
        echo.py
    graphic/
        __init__.py
        render.py
'''
#패키지 불러오기
'''
import game.sound.echo
game.sound.echo.echo_test()
#=
from game.sound import echo
echo.echo_test()
#=
from game.sound.echo import echo_test
echo_test()

from game.sound.echo import echo_test as e # echo_test함수를 e로 바꿔서 호출
e()
'''
'''
from game.sound import *
echo.echo_test()

# *는 모두(all)를 뜻함, *를 실행하기 위해서는 호출되는 파일에서 무슨 파일을 호출할지 __all__에 지정해야함
# C:/git/Python/game/sound/__init__.py
#__all__ = ['echo','echo2',aaaa'] # import *을 할 시 다음의 함수들을 호출
'''
#relative 패키지
'''
from ..sound.echo import echo_test #..의 뜻은 이전 폴더로 돌아간다는 뜻 (현재 폴더인 graphic의 이전 폴더인 게임 폴더에서 다시
                                    #sound 폴더의 echo 폴더로 들어가 echo_test를 실행하라는 뜻

def render_test()
    print("render")
    echo_test()
'''

##예외처리 : 오류 발생했을 때 어떻게 할 지 정하는 것
'''
try: #오류가 발생할 수 있는 구문
except Exception as e: #오류 발생
else: #오류 발생하지 않음
finally: #무조건 마지막에 실행
'''
#try except문
'''
try:
    4/0
except ZeroDivisionError as e: #4에서 0을 나누면 ZeroDivisionError가 나올줄 예상하고 이를 출력함, 예상 못하겠으면 Exception
    print(e)
print("일단은 작동합니다.") #try문을 사용하면 오류가 나와 프로그램이 작동을 멈춰야 할 대 임의로 실행시킴

try:
    f = open("없는 파일", 'r')
except FileNotFoundError as e: #어떤 에러가 나올지 예상할 수 없으면 FileNotFoundError자리에 Exception을 대신 사용
    print(str(e))
else: #try문이 성공하면 else문을 실행, 실패하면 except문을 실행
    data = f.read()
    print(data)
    f.close()
finally: #오류가 나건말건 무조건 실행
    f.close()
    
#오류 회피
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")
except FileNotFoundError: #오류 회피 구문
    pass
'''
#오류 일부러 발생
class Bird():
    def fly(self): #자식클래스에서 무조건 이 함수를 각각 변형해서 쓰게 하고 싶을 때 사용. 변형을 안하면 에러가 나오니 무조건 변형
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()