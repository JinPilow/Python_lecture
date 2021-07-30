from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1366x768")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
# headlesschrome으로 실행 시 user-agent 값이 변형되어 접근이 막힐 수 있으므로 user-agent 값을 별도로 지정

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# <원래 useragent 값>
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/
# 537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# <headlesschrome 시 useragent 값>
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/
# 537.36 (KHTML, like Gecko) HeadlessChrome/92.0.4515.107 Safari/537.36