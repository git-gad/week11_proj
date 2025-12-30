from models import ContactCreate
import os
import time
from pymongo import MongoClient

def get_db():
    user = os.getenv('MONGO_USER')
    password = os.getenv('MONGO_PASSWORD')
    host = os.getenv('MONGO_HOST')
    db_name = os.getenv('MONGO_DB')

    uri = f'mongodb://{user}:{password}@{host}:27017'
    client = MongoClient(uri)
    return client[db_name]

class DAL:
    db = get_db()
    contact_collection = db['contacts'] if db is not None else None
    
    @classmethod
    def get_all(cls):
        contacts = cls.contact_collection.find()
        return list(contacts)

    @classmethod
    def create_contact(cls, contact: ContactCreate):
        result = cls.contact_collection.update_one(contact.model_dump())
        return result.upserted_id
     
    @classmethod    
    def update_contact(cls, id: int, updated_contact: ContactCreate):
        result = cls.contact_collection.replace_one(
            {'_id': id},
            updated_contact.model_dump
        )
      
    @classmethod   
    def del_contact(cls, id: int):
        result = cls.contact_collection.delete_one(
            {'_id': id}
        )