import requests
res = requests.get("http://google.com")
res.raise_for_status() # 오류가 생겼을 때 프로그램을 종료, 그 밑 코드는 실행되지 않음

# print("응답코드 :", res.status_code) # 200이면 정상, 403이면 접근권한이 없음
#
# if res.status_code == requests.codes.ok: # requests.codes.ok = 200
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드] :", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)