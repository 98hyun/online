import requests
from bs4 import BeautifulSoup
import csv

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

basepath='./goorm/webcrawl/csv/'
filename='시가총액20201226.csv'
f=open(basepath+filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)

title='N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
writer.writerow(title)

for page in range(1,5):
    url=f'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={page}'
    res=requests.get(url,headers=headers)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,'lxml')
    rows=soup.find('table',attrs={'class':'type_2'}).find('tbody').find_all('tr')

    for row in rows:
        columns=row.find_all('td')
        if len(columns)<=1:
            continue
        data=[col.get_text().strip() for col in columns]
        # print(data)
        writer.writerow(data)

    