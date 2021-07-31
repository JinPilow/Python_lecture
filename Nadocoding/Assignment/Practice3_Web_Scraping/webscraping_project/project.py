from bs4 import BeautifulSoup
import requests
import re

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(idx, title, link):
    print("{}. {}".format(idx+1, title))
    print("  (링크 : {})".format(link))


def scrape_weather():
    print("[오늘의 날씨]")

    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    # 구름많음, 어제보다 0˚ 낮아요
    cast_txt = soup.find("p", attrs={"class":"cast_txt"}).get_text()

    # 현재 00℃ (최저 00 / 최고 00)
    # curr_temp = soup.find("span", attrs={"class":"todaytemp"}).get_text()
    # min_temp = soup.find("span", attrs={"class":"min"}).find("span", attrs={"class":"num"}).get_text()
    # max_temp = soup.find("span", attrs={"class":"max"}).find("span", attrs={"class":"num"}).get_text()
    curr_temp = soup.find("p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "") # 현재 온도
    min_temp = soup.find("span", attrs={"class":"min"}).get_text() # 최저 온도
    max_temp = soup.find("span", attrs={"class":"max"}).get_text() # 최고 온도

    # 오전 강수확률 00% / 오후 강수확률 00%
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    # 미세먼지 32㎍/㎥보통
    # 초미세먼지 20㎍/㎥보통
    # dust = soup.find("dl", attrs={"class":"indicator", "id":"dust"}) # 두 가지 이상의 속성 비교 가능
    # dust = soup.find("dl", attrs={"class": "indicator"}, text=["미세먼지", "초미세먼지"])
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지

    # 출력
    print(cast_txt)
    print(f"현재 {curr_temp} (최저 {min_temp} / 최고 {max_temp})")
    print(f"오전 {morning_rain_rate} / 오후 {afternoon_rain_rate}")
    print()
    print(f"미세먼지 {pm10}\n초미세먼지 {pm25}")

def scrape_headline_news():
    print("[헤드라인 뉴스]")

    url = "https://news.naver.com"
    soup = create_soup(url)
    # li 태그를 3개 까지만 찾도록 제한
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        # title = news.find("a").get_text()
        title = news.div.a.get_text().strip()
        link = url + news.find("a")["href"]
        print_news(idx, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")

    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(idx, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")

    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences) // 2:]: # 8문장이 있다고 가정할 때, 5~8까지 슬라이싱
        print(sentence.get_text().strip())

    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences) // 2]: # 8문장이 있다고 가정할 때, 1~4까지 슬라이싱
        print(sentence.get_text().strip())
    print()

if __name__ == "__main__": # 이 파일을 직접 실행해야지만 동작함. 다른 함수에 의해 호출되면 동작하지 않음
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 가져오기
    scrape_english() # 오늘의 영어 회화 가져오기