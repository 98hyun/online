import requests
from bs4 import BeautifulSoup

url='https://comic.naver.com/webtoon/list.nhn?titleId=675554'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')

# 만화 제목, 링크
# webtoons=soup.find_all('td',attrs={'class':'title'})
# for webtoon in webtoons:
#     title=webtoon.a.get_text()
#     link="https://comic.naver.com"+webtoon.a['href']
#     print(title,link)

# 만화 평점.

webtoons=soup.find_all('div',attrs={'class':'rating_type'})

for webtoon in webtoons:
    rate=webtoon.span.em.get_text()
    num=webtoon.strong.get_text()
    print(rate,num)