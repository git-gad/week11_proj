from fastapi import APIRouter, Depends
from data_interactor import DAL, DB_Connection
from models import Contact

router = APIRouter()

dal = DAL()

@router.get('/')
def get_all_contacts(db=Depends(DB_Connection.get_db)):
    return dal.get_all(db)

@router.post('/')
def add_contact(contact: Contact, db=Depends(DB_Connection.get_db)):
    contact_id = dal.create_contact(db, contact)
    return {'message': 'success', 'id': contact_id}

@router.put('/{id}')
def change_contact(id, updated_contact: Contact, db=Depends(DB_Connection.get_db)):
    dal.update_contact(db, id, updated_contact)
    return {'message': 'success'}

@router.delete('/{id}')
def delete_contact(id, db=Depends(DB_Connection.get_db)):
    dal.del_contact(db, id)
    return {'message': 'success'}