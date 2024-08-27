import pymongo

url = 'mongodb://abbas:1@mongodb:27017'
client = pymongo.MongoClient(url)

db = client['mdm_logs']