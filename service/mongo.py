from config import mongo
from bson import ObjectId


def generate_id():
    return str(ObjectId())

def get_existing(merchantName, productName, brand):
    client, collection = mongo.get_mongo_collection("products")
    result = False
    with client:
        if collection.find_one({
            "merchantName": merchantName,
            "productName": productName,
            "brand": brand
        }):
            result = True
    return result


def insert_products(data: list):
    client, collection = mongo.get_mongo_collection("products")
    items = []
    for item in data:
        if get_existing(item.get('merchantName'), item.get('productName'), item.get('brand')):
            continue
        item['_id'] = generate_id()
        items.append(item)
    with client:
        if len(items) > 0:
            collection.insert_many(items)
    