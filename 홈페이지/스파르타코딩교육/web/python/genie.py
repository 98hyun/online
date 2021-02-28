from bs4 import BeautifulSoup
import requests

from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.firstDb

url='https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

data=requests.get(url,headers=header)
soup=BeautifulSoup(data.text,"html.parser")

lst=soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')

for idx,l in enumerate(lst,start=1):
    info=l.select_one('td.info')
    song=info.select_one('a').text.strip()
    singer=l.select_one('td.info > a.artist.ellipsis').text
    doc={
        'num':idx,
        'song':song,
        'singer':singer
    }
    db.genie.insert_one(doc)
    print(idx,song,singer)
