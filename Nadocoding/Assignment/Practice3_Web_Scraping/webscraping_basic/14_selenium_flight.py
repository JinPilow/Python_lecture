from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 전체화면으로 키우기

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

# 가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [0] : 이번달 [1] : 다음달
# browser.find_elements_by_link_text("28")[1].click()

# 이번달 30일, 다음달 23일 선택
browser.find_elements_by_link_text("30")[0].click()
browser.find_elements_by_link_text("23")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/a[2]/span").click()
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/div[2]/table[1]/tbody/tr[1]/td[1]/a").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 아래 element가 나올 때까지 브라우저를 최대 10초 동안 기다려 로딩시간에 에러 발생하는 것을 방지
    # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)