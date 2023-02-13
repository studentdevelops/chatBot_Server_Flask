from sqlalchemy import Column, String, LargeBinary
from DataModels.BaseDM import BaseDM
class UserDM(BaseDM):
    __tablename__ = "Users"
    email = Column(String(55),unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
    password_salt = Column(LargeBinary, nullable=False)

