import logging
from pymongo import MongoClient
from config import DB
from bson.objectid import ObjectId


def insert_items_mongo(item_info_json, database=DB):
    """

    :param item_info_json:
    :param database:
    :return:
    """
    try:
        client = MongoClient()
        database = client[database]
        db_response = database.complex.insert_one(item_info_json)
        item_id = str(db_response.inserted_id)
        logging.info("Inserted into database element {}.".format(item_id))
        response = {'item_id': item_id}
        client.close()
    except Exception as exp:
        logging.exception("Could not connect to the MongoDB and insert item.")
        response = {}
    return response


def get_items_mongo(query={}, database=DB):
    """

    :param item_info_json:
    :param database:
    :return:
    """
    try:
        client = MongoClient()
        database = client[database]
        response = [i for i in database.complex.find(query)]
        client.close()
    except Exception as exp:
        logging.exception("Could not connect to the MongoDB and insert item.")
        response = []
    return response


def get_item_by_id(_id, database=DB):
    try:
        client = MongoClient()
        database = client[database]
        response = database.complex.find_one({'_id': ObjectId(_id)})
        client.close()
    except Exception as exp:
        logging.exception("Could not connect to the MongoDB and insert item.")
        response = {}
    return response    
