from sqlalchemy import Column, Integer, String, Boolean, Float, Text, Boolean
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from DataModels.BaseDM import BaseDM
from DataModels.UserRegDM import UserRegDM
class UserChatHistoryDM(BaseDM):
    __tablename__ = 'UserChatHistory'
    Question = Column(String, nullable=False)
    Answer = Column(String, nullable=False)
    UserId = Column(String(36), ForeignKey(UserRegDM.SysId), nullable=False)
    User = relationship(UserRegDM, backref=backref("UserChatHistory"))
