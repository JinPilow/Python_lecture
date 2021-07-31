import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status() # 오류가 생겼을 때 프로그램을 종료, 그 밑 코드는 실행되지 않음
with open("nadocoding.html", "w", encoding = "utf8") as f:
    f.write(res.text)
# 권한이 없는 페이지에 접속할 때 사용. Google에 본인의 User-Agent 복사하여 붙여넣기