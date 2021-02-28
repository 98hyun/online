import requests
from bs4 import BeautifulSoup
import re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


for year in range(2019,2015,-1):

    url=f'https://search.daum.net/search?w=tot&DA=BFT&nil_profile=fix_similar&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'

    res=requests.get(url,headers=headers)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,'lxml')

    imgs=soup.find_all('img',attrs={'class':'thumb_img'})

    for idx,img in enumerate(imgs):
        img=img['src']
        if not img.startswith('//'):
            continue
        img='http:'+img
        img_res=requests.get(img)
        img_res.raise_for_status()

        if idx>=5:
            break

        with open(f'./goorm/webcrawl/img/movie_{year}_{idx+1}.png','wb') as f:
            f.write(img_res.content)