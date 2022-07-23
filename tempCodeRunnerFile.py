import pymongo

client = pymongo.MongoClient("mongodb+srv://ChiragKapoor:chirag31kapoor@uwu.hsqq1w1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"chirag",
    "email" : "chirag@kapoor",
    "surname" : "kapoor"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
