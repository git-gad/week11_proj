from models import ContactCreate
import os
import time
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import json_util, ObjectId
import json

load_dotenv()

host = os.getenv('MONGO_HOST')
db_name = os.getenv('MONGO_DB')
URI = f'mongodb://{host}:27017'
CONTACTS_COLL = "contacts"

class DB_Connection:
    client = None
    
    @classmethod
    def connect_client(cls):
        if cls.client is None:
            cls.client = MongoClient(URI)
            cls.client.admin.command("ping")
            print("Established mongodb connection")    
        return cls.client
    
    @classmethod
    def get_db(cls):
        if cls.client is None:
            cls.client = cls.connect_client()
        return cls.client[db_name]

class DAL:
    @classmethod
    def get_all(cls, db):
        contacts = db[CONTACTS_COLL].find()
        response = contacts
        response = json.loads(json_util.dumps(response))
        return response

    @classmethod
    def create_contact(cls, db, contact: ContactCreate):
        contact = contact.model_dump()
        result = db[CONTACTS_COLL].insert_one(contact)    
        return str(result.inserted_id)
     
    @classmethod    
    def update_contact(cls, db, id: str, updated_contact: ContactCreate):
        updated_contact = updated_contact.model_dump()
        result = db[CONTACTS_COLL].replace_one(
            {'_id': ObjectId(id)},
            updated_contact
        )
      
    @classmethod   
    def del_contact(cls, db, id: str):
        result = db[CONTACTS_COLL].delete_one(
            {'_id': ObjectId(id)}
        )