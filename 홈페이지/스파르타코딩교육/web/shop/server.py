from flask import Flask,request,jsonify,render_template
app=Flask(__name__)

from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.firstDb

@app.route('/')
def index():
    return render_template('shop.html')

@app.route('/shop',methods=['post'])
def save():
    email=request.form['email']
    phone=request.form['phone']

    data={
        'email':email,
        'phone':phone
    }
    
    db.shop.insert_one(data)
    return jsonify({'result':'success'})

@app.route('/shop',methods=['get'])
def post():
    data=list(db.shop.find({},{'_id':0}))
    return jsonify({'result':'success','data':data})

if __name__=='__main__':
    app.run(debug=True)