from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# browser = webdriver.Chrome("C:/git/Python/Python_project2/chromedriver.exe")
browser = webdriver.Chrome("./chromedriver.exe")
# browser.get("http://naver.com")

# 네이버 로그인 버튼 클릭하기 / class name으로 찾기
# elem = browser.find_element_by_class_name("link_login")
# elem.click() # 클릭
# browser.back() # 뒤로가기
# browser.forward() # 앞으로가기
# browser.refresh() # 새로고침

# 네이버에 나도코딩 검색 / id로 찾기
# elem = browser.find_element_by_id("query")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# a element의 href 속성 가져오기 / tag_name으로 찾기
# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#     hyper = e.get_attribute("href")
#     print(hyper)

# 다음에 나도코딩 검색하기 / name으로 찾기
# browser.get("http://daum.net")
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# # elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# elem.click()
# browser.close() # 현재 열려있는 탭만 닫음
# # browser.quit() # 모든 브라우저 종료

# -----------------------------------

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. ID와 PASSWORD 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source) # 지금 페이지에 있는 모든 html 문서를 출력

# 7. 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료