import pymongo

def mongo_connect():
    client = pymongo.MongoClient("mongodb+srv://yskim:<password>@cluster0.mxqeo.gcp.mongodb.net/test?retryWrites=true&w=majority")
    return client
