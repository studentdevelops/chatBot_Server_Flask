from sqlalchemy import  Column, String, LargeBinary , DateTime ,ForeignKey ,create_engine
from sqlalchemy.orm import relationship,backref
from DataModels.BaseDM import BaseDM,Base
from DataModels.UserDM import UserDM
import datetime
class UserHistoryDM(BaseDM):
    __tablename__ = "UserHistories"
    CreatedDate = Column(DateTime, default=datetime.datetime.utcnow,nullable=True)
    Question = Column(String,nullable=False)
    Answer = Column(String,nullable=False)
    UserId = Column(String(36),ForeignKey(UserDM.SysId),nullable=False)
    User = relationship(UserDM,backref=backref("UserHistory"))
