'''


#12
result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)


#13
numstring = input("숫자를 입력하시오: ")
result = []

def iseven(n):
    if n%2 == 0:
        return 1
    else:
        return 0

def DashInsert(numstring):
    for i in range(len(numstring)):
        if i == 0:
            result.append(numstring[i])
            pass
        elif iseven(int(numstring[i])) != iseven(int(numstring[i-1])):
            result.append(numstring[i])
            pass
        elif iseven(int(numstring[i])) and iseven(int(numstring[i-1])):
            result.append("*"+numstring[i])
        elif not iseven(int(numstring[i])) and not iseven(int(numstring[i-1])):
            result.append("-"+numstring[i])
    b = "".join(result)
    return b

print(DashInsert(numstring))


#14
#입력 예시: aaabbcccccca
#출력 예시: a3b2c6a1

data = input("문자를 입력하시오: ")
temp = []
result = []

for i in range(len(data)):
    if i == len(data) - 1:
        result.append(temp[0])
        result.append(str(data.count(data[i])))
        temp.clear()
    elif data[i] == data[i+1]:
        temp.append(data[i])
    elif data[i] != data[i+1]:
        result.append(temp[0])
        result.append(str(data.count(data[i])))
        temp.clear()
tot = "".join(result)

print(tot)


#15
#입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
#출력 예시: True False False True False

data = input("숫잡를 입력하시오: ")
result = []

for i in data:
    if i not in result:
        result.append(i)
    else:
        print(False)
if len(result) == 10:
    print(True)


#16
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def read(s):
    result = []
    words = s.split("  ")
    for word in words:
        letter = word.split(" ")
        for i in letter:
            result.append(dic[i])
        if not word == words[-1]:
            result.append(" ")
        sentence = "".join(result)
    return sentence
print(read(".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"))


#17
import re

p = re.compile("a[.]{3,}b")

print (p.match("acccb"))    # None
print (p.match("a....b"))   # 매치 객체 출력
print (p.match("aaab"))     # None
print (p.match("a.cccb"))   # None


#18
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start() + m.end())


#19
import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

p = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = p.sub("\g<1>-####", s)
print(result)
'''

#20
import re

pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))