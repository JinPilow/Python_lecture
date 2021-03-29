def add(a,b):
    return a+b
def sub(a,b):
    return a-b

print(__name__) #현재 파일 이름
if __name__ == "__main__": #__main__은 현재 내가 위치한 파일
    print(add(3,4))
    print(add(1,2))

