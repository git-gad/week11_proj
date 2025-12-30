from models import ContactCreate
import os
import time
from mysql.connector import connect, Error
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
    @staticmethod
    def get_all():
        
        return rows

    @staticmethod
    def create_contact(contact: ContactCreate):
        conn = get_connection()
        cursor = conn.cursor()
        query = '''INSERT INTO contacts (first_name, last_name, phone_number) 
                VALUES (%s, %s, %s)'''
        data = (contact.first_name, contact.last_name, contact.phone_number)
        cursor.execute(query, data)
        id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return id  
     
    @staticmethod    
    def update_contact(id: int, updated_contact: ContactCreate):
        conn = get_connection()
        cursor = conn.cursor()
        query = '''UPDATE contacts 
                SET first_name = %s, last_name = %s, phone_number = %s
                WHERE id = %s'''
        data = (updated_contact.first_name, updated_contact.last_name, updated_contact.phone_number, id)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
      
    @staticmethod   
    def del_contact(id: int):
        conn = get_connection()
        cursor = conn.cursor()
        query = '''DELETE FROM contacts 
                WHERE id = %s'''
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()