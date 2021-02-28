# load library
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload
from openpyxl import Workbook

# simple structure
driver=webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
driver.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석')
time.sleep(3)

# excel
wb=Workbook()
ws=wb.active
ws.title="articles"
ws.append(['제목','링크'])

# result
res=driver.page_source

soup=BeautifulSoup(res,'html.parser')

articles=soup.select('ul.type01 li dl dt')

# scrap
for article in articles:
    tag=article.select_one('a')
    
    title=tag.text
    url=tag['href']
    ws.append([title,url])
    
# quit
driver.quit()
wb.save('article.xlsx')