from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.firstDb                       # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    memos=list(db.memo.find({},{'_id':0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'memos':memos})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    url=request.form['url']
    comment=request.form['comment']
    # 2. meta tag를 스크래핑하기
    data=requests.get(url,headers=headers)
    soup=BeautifulSoup(data.text,'html.parser')

    simage=soup.select_one('meta[property="og:image"]')
    stitle=soup.select_one('meta[property="og:title"]')
    sdescription=soup.select_one('meta[property="og:description"]')

    image=simage['content']
    title=stitle['content']
    description=sdescription['content']

    memos={
        'title':title,
        'image':image,
        'description':description,
        'url':url,
        'comment':comment
    }
    # 3. mongoDB에 데이터 넣기
    db.memo.insert_one(memos)
    return jsonify({'result': 'success','msg':'POST'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)