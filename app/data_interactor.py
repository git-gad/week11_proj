from models import Contact
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

host = os.getenv('MONGO_HOST', 'mongo-noauth')  
db_name = os.getenv('MONGO_DB', 'testdb')

CONTACTS_COLL = "contacts"

class DB_Connection:
    client = None
    
    @classmethod
    def connect_client(cls):
        if cls.client is None:
            cls.client = MongoClient(f"mongodb://{host}:27017/")
            cls.client.admin.command("ping")
            print("Established mongodb connection") 
            print("MONGO URI >>>", f"mongodb://{host}:27017/")
        return cls.client

    @classmethod
    def get_db(cls):
        if cls.client is None:
            cls.client = cls.connect_client()
        return cls.client[db_name]

class DAL:
    @classmethod
    def get_all(cls, db):
        contacts = list(db[CONTACTS_COLL].find())
        for contact in contacts:
            contact["_id"] = str(contact["_id"])
        return contacts

    @classmethod
    def create_contact(cls, db, contact: Contact):
        contact = contact.model_dump()
        result = db[CONTACTS_COLL].insert_one(contact)    
        return str(result.inserted_id)
     
    @classmethod    
    def update_contact(cls, db, id, updated_contact: Contact):
        updated_contact = updated_contact.model_dump()
        result = db[CONTACTS_COLL].replace_one(
            {'_id': ObjectId(id)},
            updated_contact
        )
      
    @classmethod   
    def del_contact(cls, db, id):
        result = db[CONTACTS_COLL].delete_one(
            {'_id': ObjectId(id)}
        )