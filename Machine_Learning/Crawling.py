from bs4 import BeautifulSoup
from urllib.request import urlopen
with urlopen('https://www.naver.com/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    for anchor in soup.select('span.ah_k'):
        print(str(i) + "위: " + anchor.get_text())
        i = i + 1
