from flask import Flask,render_template,jsonify,request
app=Flask(__name__)

from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.firstDb

# html
@app.route('/')
def home():
    return render_template('index.html')

# api
@app.route('/reviews',methods=['post'])
def writeReview():
    title=request.form['title']
    author=request.form['author']
    review=request.form['review']
    # db 추가 내용.
    reviews={
        'title':title,
        'author':author,
        'review':review
    }
    db.book.insert_one(reviews)
    ## 보내고 싶은 내용.
    return jsonify({'result':'success','msg':'post'}) 

@app.route('/reviews',methods=['get'])
def readReview():
    reviews=list(db.book.find({},{'_id':0}))
    return jsonify({'result':'success','reviews':reviews})

if __name__=='__main__':
    app.run(debug=True)
