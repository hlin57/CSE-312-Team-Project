import pymongo
client = pymongo.MongoClient(port=27017)
db=client.web_project
user_identity = db.user_identity
user_identity_key={'username':'','email':'','shadow':''}.keys()
def insert(insert_dict):
    if insert_dict.keys() == user_identity_key:
        user_identity.insert_one(insert_dict)

def find(target):
    for x in user_identity.find({},{"_id": 0,'username':1,'email':1,'shadow':1}):
        print(x)
    

if __name__ == "__main__":
    test_case_1 = {'username':'hh','email':'test','shadow':'asdawzx'}
    #insert(test_case_1)
    find(test_case_1)
