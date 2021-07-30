# Quiz) 부동산 매물 (송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오.
#
# [조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보
#
# [출력 결과]
# ========== 매물 1 ==========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000(만원)
# 동: 214동
# 층 : 고/23
# ========== 매물 2 ==========
#
# [주의 사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1366x768")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://realty.daum.net/home/apt/danjis/38487"
browser.get(url)

view_btn = browser.find_element_by_xpath("//*[@id='__next']/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/div[2]/div/div[4]/div/div[2]/div[3]/div/div[1]/div[1]")
view_btn.click()

soup = BeautifulSoup(browser.page_source, "lxml")


contents = soup.find("div", attrs={"class":"rn-1oszu61 rn-14lw9ot rn-1efd50x rn-14skgim rn-rull8r rn-mm0ijv rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-6koalj rn-16y2uox rn-1wbh5a2 rn-1mlwlqe rn-eqz5dr rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-ifefl9 rn-bcqeeo rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bnwqim rn-1lgpqti"})
print(len(contents))

sales = soup.find("div",attrs={"class":"rn-1oszu61 rn-1niwhzg rn-1efd50x rn-14skgim rn-rull8r rn-mm0ijv rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-6koalj rn-1qe8dj5 rn-1mlwlqe rn-eqz5dr rn-61z16t rn-p1pxzi rn-11wrixw rn-bcqeeo rn-11yh6sk rn-buy8e9 rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bnwqim rn-1lgpqti"}).find_all("div", attrs={"class":"rn-1oszu61 rn-1efd50x rn-14skgim rn-rull8r rn-mm0ijv rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-6koalj rn-16y2uox rn-1wbh5a2 rn-1mlwlqe rn-eqz5dr rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-ifefl9 rn-bcqeeo rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bnwqim rn-1lgpqti"})

for idx, sale in enumerate(sales):
    print("="*10 + " 매물 " + str(idx+1) + " " + "="*10)
    type = sale.find("div", attrs={"class":"rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-11t4n93 rn-1471scf rn-143r1dj rn-o11vmf rn-ebii48 rn-vw2c0b rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bauka4 rn-q42fyq rn-qvutc0"})
    area = sale.find("div", attrs={"class":"rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-11t4n93 rn-1471scf rn-143r1dj rn-n6v787 rn-o11vmf rn-ebii48 rn-gul640 rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bauka4 rn-q42fyq rn-qvutc0"})
    price = sale.find("div", attrs={"class":"rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-11t4n93 rn-1471scf rn-143r1dj rn-n6v787 rn-o11vmf rn-ebii48 rn-vw2c0b rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bauka4 rn-q42fyq rn-qvutc0"})
    floor = sale.find("div", attrs={"class":"rn-13yce4e rn-fnigne rn-ndvcnb rn-gxnn5r rn-deolkf rn-11t4n93 rn-1471scf rn-143r1dj rn-n6v787 rn-o11vmf rn-ebii48 rn-gul640 rn-1mnahxq rn-61z16t rn-p1pxzi rn-11wrixw rn-wk8lta rn-9aemit rn-1mdbw0j rn-gy4na3 rn-bauka4 rn-q42fyq rn-qvutc0"})
    print(f"거래 : {type.get_text()}")
    print(f"면적 : {area.get_text()}")
    print(f"가격 : {price.get_text()}")
    print(f"층 : {floor.get_text()}")

browser.quit()