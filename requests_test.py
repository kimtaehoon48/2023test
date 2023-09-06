import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
html = response.text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.html.body.h1)

result = soup.select('.news_tit')
# for i in result:
    # title = i.text
    # url = i.attrs['href']
    # print(title,url)