'''
##정규표현식
import re
data = """
park 800905-1049118
kim 700905-1059118
"""

pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-******",data))

"""
[a-d] : a부터 d 중 하나와 매치
[0-9] : 0부터 9 중 하나와 매치

a.b : '.'은 줄바꿈(\n)을 제외한 모든 문자와매치
ex) aab,a0b 등등 매치

ca*t : a가 0번 이상 매치
ex) ct, cat, caaat
ca+t : a가 무조건 1번 이상매치
ex) cat, caat, caaat
ca{2}t : {}안의 수 만큼 반복
ex) caat
ca{2,5}t : a가 {}의 첫번째 수 이상 두번째 수 이하 반복
ex) caat,caaat,caaaat,caaaaat 2이상 5이하

ab?c : 0회 혹은 1회 #?=={0,1} 같은 표현
ex) ac, abc


#MATCH
import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(m.group()) #매치된 문자열 return
print(m.start()) #매치된 문자열의 시작위치 return
print(m.end()) #매치된 문자열의 끝위치 return
print(m.span()) #매치된 문자열의 (시작, 끝)에 해당되는 튜플을 return


m=p.match("3 python")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())


#SEARCH : 전부 다 match 하지 않더라도 match하는 부분을 찾아서 return
import re
p = re.compile('[a-z]+')
m = p.search("python")
print(m)
m = p.search("3 python")
print(m)


#FINDALL : 일치하는 string을 list에 담아서 return
import re
p = re.compile('[a-z]+')
m = p.findall("life is too short")
print(m)


#FINDITER
import re
p = re.compile('[a-z]+')
m = p.finditer("life is too short")
print(m)
for i in m:
    print(i)


##컴파일 옵션
#DOTALL, S
import re
p = re.compile('a.b', re.DOTALL) #DOTALL은 '.'이 줄바꿈도 포함하도록 만듦, re.S로도 사용 가능
m = p.match('a\nb')
print(m)


#IGNORECASE, I
import re
p = re.compile('[a-z]', re.I) #대소문자를 무시하고 매치 가능
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))


#MULTILINE, M
import re
p = re.compile("^python\s\w+", re.M) #re.M이 있으면 data의 각각의 줄이 새로운 줄로 여겨져 결과가 달라짐
#^python : 맨처음 문자가 python
#\s : 공백
#\w : 알파벳, 숫자, _ 중 하나

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
'''

#VERBOSE, X
import re
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
&[#]                        # Start of a numeric entity reference
(                           
      0[0-7]+               #Octal form
    | [0-9]+                #Decimal form
    | x[0-9a-fA-F]+         #Hexadecimal form
)
;                           #Trailing semicolon
""",re.VERBOSE) #공백을 제거해서 컴파일이되도록 해주는 기능, 하나씩 뜯어 설명 넣어줄 때 사용

##백슬래시 문제
'''
\s : 공백을 의미
\section을 입력하면 \s ection으로 읽히므로 오류
따라서
p = re.compile('\\section') #Python 에서는 백슬래시 두개를 한개로 자동 변환해주므로 오류

p = re.compile('\\\\seciotn')
또는
p = re.compile(r'\\section') # r: 로우스트링


'''