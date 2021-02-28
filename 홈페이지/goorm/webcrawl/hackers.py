# library
from bs4 import BeautifulSoup
import requests

# config
url='https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

# ready
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')

speaking=soup.find_all('div',attrs={'class':'conv_txtBox'})

# 한글지문 
# 오늘의 표현 
today_ko_title=speaking[0].find('b',attrs={'class':'conv_txtTitle'}).get_text() 
today_ko_content=speaking[0].find('div',attrs={'class':'conv_txt'}).get_text()
# 영어지문
today_eng_title=speaking[1].find('b',attrs={'class':'conv_txtTitle'}).get_text()
today_eng_content=speaking[1].find('div',attrs={'class':'conv_txt'}).get_text()

print('-'*60)
print("Today's expression")
print("="*60)
print(today_eng_content.replace('     ','').strip())
print("-"*60)
print("오늘의 표현")
print("="*60)
print(today_ko_content.replace('     ','').strip())
