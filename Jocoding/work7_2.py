'''
##정규표현식 - 메타문자
# | : or
import re
p = re.compile('Crow|Serve')
m = p.match('CrowHello')
print(m)


# ^ : 시작 문자
import re
print(re.search('^Life','Life is too short'))
print(re.search('^Life','My Life'))


# $ : 끝 문자
import re
print(re.search('short$','Life is too short'))
print(re.search('short$','Life  is too short, you need python'))


# \b : 공백
import re
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))


##그룹핑 ()
import re
p = re.compile('(ABC)+')    #그룹으로 묶지 않고 쓰면 C만 반복, 묶었기 때문에 ABC반복
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-5678")
print(m.group(1))

p = re.compile(r'(\b\w+)\s+\1') #\1은 앞에 있는 그루핑된 항목의 결과를 가져옴
print(p.search('Paris in the the spring').group())


#그룹핑된 문자열에 이름 붙이기 ?P<name>
import re
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))


import re
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)') #\1과 같은 결과
print(p.search('Paris in the the spring').group())

#전방탐색: 긍정형 (?=)
import re
p = re.compile(".+:(?=:)")  #검색 조건에는 :이 포함되나 검색 결과에는 :이 return되지 않음
m = p.search("http://google.com")
print(m.group())


#전방탐색: 부정형 (?!)
import re
p = re.compile(".*[.](?!bat$).*$",re.M) #괄호에 있는 문자열이 제외된 문자열 탐색
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)
'''

#문자열 바꾸기 sub
import re
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))


#Greedy vs Non-Greedy
import re
s = '<html><head><tile>Title</title>'
print(re.match('<.*>',s).group())   #Greedy
print(re.match('<.*?>',s).group()) #Non Greedy #?를 쓰게 되면 최소한으로 반복하겠다는 뜻