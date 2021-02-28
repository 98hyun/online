import requests
from bs4 import BeautifulSoup

url='https://comic.naver.com/index.nhn'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')
# print(soup.title.get_text()) # text 얻기
# print(soup.a.attrs) # 속성 보기
# print(soup.a['href'])

# print(soup.find('a',attrs={'class':'Nbtn_upload'})) # 태그값이 attrs 인 값 찾을수있다.
# print(soup.find(attrs={'class':'Nbtn_upload'})) # 태그가 없을 때

# rank1=soup.find('li',attrs={'class':'rank01'})
# # print(rank1.a.get_text()) # li 안의 a 의 text
# rank2=rank1.next_sibling.next_sibling
# rank3=rank2.next_sibling.next_sibling

# # print(rank2==rank3.previous_sibling.previous_sibling)

# rank2=rank1.find_next_sibling('li') # 그뒤에 하나
# rank3=rank2.find_next_siblings('li') # 그 뒤에 모든 
# print(rank3)
url='https://comic.naver.com/webtoon/weekday.nhn'

res=requests.get(url,headers=headers)

soup=BeautifulSoup(res.text,'lxml')

webtoons=soup.find_all('a',attrs={'class':'title'})

for webtoon in webtoons:
    print(webtoon.get_text())