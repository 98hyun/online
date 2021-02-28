import requests
from bs4 import BeautifulSoup
import re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

for page in range(1,6):

    url=f'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='

    res=requests.get(url,headers=headers)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,'lxml')

    items=soup.find_all('li',attrs={'class':re.compile('^search-product')})

    for item in items:

        ads=item.find('span',attrs={'class':'ad-badge-text'})
        if ads:
            # print("광고상품 제외")
            continue

        link='https://www.coopang.com'+item.a['href']
        name=item.find('div',attrs={'class':'name'}).get_text()
        
        if 'Apple' in name:
            # print("애플 제품 제외")
            continue
        value=item.find('strong',attrs={'class':'price-value'}).get_text()
        rate=item.find('em',attrs={'class':'rating'})
        if rate:
            rate=rate.get_text()
        else:
            # print("평점 없는 제품 제외")
            continue

        review=item.find('span',attrs={'class':'rating-total-count'})
        if not review:
            # print("review 없는 제품 제외")
            continue
        else:
            review=review.get_text()

        if float(rate)>=4.5 and int(review[1:-1])>=100:
            print(f'{name}')
            print(f'{rate}점 {review[1:-1]}명 리뷰')
            print(f'바로가기 : {link}')
            print(f'{value}원')
            print('='*100)
        else:
            # print("인증 안됨")
            continue