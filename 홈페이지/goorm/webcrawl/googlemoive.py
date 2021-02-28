# import requests
# from bs4 import BeautifulSoup

# url='https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=en&gl=US'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'Accept-Language':'ko-KR,ko'
#     }

# res=requests.get(url,headers=headers)
# res.raise_for_status()
# soup=BeautifulSoup(res.text,'lxml')

# movies=soup.find_all('div',attrs={'class':'ImZGtf mpg5gc'})

# # for movie in movies:
# #     title=movie.find('div',attrs={'class':'WsMG1c nnK0zc'}).get_text()
# #     genre=movie.find('div',attrs={'class':'KoLSrc'}).get_text()

# #     print(title,genre)
# #     break

# with open('movie.html','w',encoding='utf-8-sig') as f:
#     f.write(soup.prettify())


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# config
browser=webdriver.Chrome('./goorm/webcrawl/chromedriver_win32/chromedriver.exe')

url='https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=en&gl=US'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept-Language':'ko-KR,ko'
    }

res=requests.get(url,headers=headers)
res.raise_for_status()

browser.get(url)

# scroll
prev_scroll=browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

while True:
    # scroll 내리기
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 대기
    time.sleep(3)

    # 현재 scroll
    current_scroll=browser.execute_script('return document.body.scrollHeight')

    # 조건
    if current_scroll==prev_scroll:
        break

    # 수정.
    prev_scroll=current_scroll
     
# browser.close()

soup=BeautifulSoup(browser.page_source,'lxml')

movies=soup.find_all('div',attrs={'class':'ImZGtf mpg5gc'})

for movie in movies:
    title=movie.find('div',attrs={'class':'WsMG1c nnK0zc'}).get_text()
    genre=movie.find('div',attrs={'class':'KoLSrc'}).get_text()

    print(title,genre)

