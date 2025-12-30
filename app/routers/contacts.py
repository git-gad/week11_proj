from fastapi import APIRouter, Depends
from data_interactor import DAL, DB_Connection
from models import ContactCreate

router = APIRouter()

dal = DAL()
db_connection = DB_Connection()
client = db_connection.connect_client()
db = db_connection.get_db()

@router.get('/')
def get_all_contacts():
    return dal.get_all(db)

@router.post('/')
def add_contact(contact: ContactCreate):
    id = dal.create_contact(db, contact)
    return {'message': 'success', 'id': id}

@router.put('/{id}')
def change_contact(id, updated_contact: ContactCreate):
    dal.update_contact(db, id, updated_contact)
    return {'message': 'success'}

@router.delete('/{id}')
def delete_contact(id):
    dal.del_contact(db, id)
    return {'message': 'success'}