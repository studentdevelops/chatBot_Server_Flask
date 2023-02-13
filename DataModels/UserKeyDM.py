from sqlalchemy import Column, String,INT,ForeignKey
from DataModels.BaseDM import BaseDM
from  sqlalchemy.orm import relationship,backref
from DataModels.UserDM import UserDM
class UserKeyDM(BaseDM):
    __tablename__ = "UserKeys"
    TotalRequests = Column(INT,nullable=False)
    UserId = Column(String(36), ForeignKey(UserDM.SysId), nullable=False,unique=True)
    User = relationship(UserDM, backref=backref("UserKey"))
    #ApiKey = Column(String(),nullable=False)
