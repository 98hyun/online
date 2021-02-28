'''from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client.firstDb
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})'''

## q1 find 
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.firstDb

target=db.movies.find_one({
    'title':'매트릭스'
})

# print(target['star'])

# q2 find same star on 매트릭스.
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.firstDb
target=db.movies.find_one({
    'title':'매트릭스'
})
targets=list(db.movies.find({
    'star':target['star']
}))

for t in targets:
    # print(t['title'])

# q3 update ( expected indent block )
    db.movies.update_many({'star':target['star']},{'$set':{'star':0}}) 