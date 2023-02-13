from sqlalchemy import and_,or_
from DataModels import *
import os
import hashlib
from DataModels.BaseDM import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mssql+pyodbc://' + 'LAPTOP-LC07V53A/CPING?' + 'driver=SQL+Server+Native+Client+11.0')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session = Session()


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()

    return salt, hashed_password


def verify_password(password, salt, stored_hashed_password):
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return hashed_password == stored_hashed_password.decode()

def VerifyExits(TableName,whereclause):
    #Checks whther Data exists in column on bassis of where clause provided dictionary of where clause
    conditions = []
    for key, value in whereclause.items():
        conditions.append(getattr(TableName, key) == value)
    query = Session.query(TableName).filter(or_(*conditions)).all()
    if query is None or not query or len(query)==0:
        return False
    else:
        return True


