import os
import hashlib
import uuid
import json

from DataModels.UserRegDM import UserRegDM
from DataModels.UserDM import User
from LogicComponent.AppHelper import Session
def to_dict(model):
    """
    Convert a SQLAlchemy class to a dictionary.
    """
    dictionary = {}
    for column in model.__table__.columns:
        dictionary[column.name] = str(getattr(model, column.name))
    return dictionary

def to_json(model):
    """
    Convert a SQLAlchemy class to a JSON string.
    """
    return json.dumps(to_dict(model))
def CheckUser(email):
    return Session.query(UserRegDM).filter(UserRegDM.email == email).first() is not None

def ReturnUser(email,password):
    if CheckUser(email):
        user = Session.query(UserRegDM).filter(UserRegDM.email==email).first()
        if verify_password(password,user.password_salt,user.password):
            UserDet = Session.query(User).filter(User.UserId == user.SysId).first()
            if(UserDet is not None):
                return {'success':user.SysId,'Details':to_json(UserDet)}
            return {'success': 'failed' }
        else:
            return {'success':'false'}
def CreateUser(email,password):
    if not CheckUser(email):
        s,hashpassowrd=hash_password(password)
        print(s)
        sysid=str(uuid.uuid4())
        user = UserRegDM(SysId=sysid,email=email,password=bytes(hashpassowrd,'utf-8'),password_salt=s)
        Session.add(user)
        Session.commit()
        return {'success': 'true','UserId':sysid}
    else:
        return {'Error':'Inavild Email Or User Exists'}
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()

    return salt, hashed_password
def verify_password(password, salt, stored_hashed_password):
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return hashed_password == stored_hashed_password.decode()


#print(ReturnUser('mufad','123'))