from sqlalchemy import Column, Integer, String, Boolean, Float, Text, Boolean
#from sqlalchemy.ext.declarative import declarative_base
from DataModels.BaseDM import BaseDM
from DataModels.UserRegDM import UserRegDM
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class User(BaseDM):
    __tablename__ = 'users'
    name = Column(String(255), nullable=False)
    Age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    bmi = Column(Float, nullable=True)
    bmr = Column(Integer,nullable=True)
    baseline_cancer = Column(Integer, nullable=True)
    baseline_pulmonary = Column(Integer, nullable=True)
    baseline_dementia = Column(Integer, nullable=True)
    baseline_diabetes = Column(Integer, nullable=True)
    baseline_digestive = Column(Integer, nullable=True)
    baseline_osteoart = Column(Integer, nullable=True)
    baseline_cvd = Column(Integer, nullable=True)
    baseline_psych = Column(Integer, nullable=True)
    q9 = Column(Integer, nullable=True)
    q10 = Column(Integer, nullable=True)
    mi = Column(Text, nullable=True)
    ailment = Column(Text, nullable=True)
    surgery = Column(Integer,nullable=True)
    medical_assistance = Column(Integer, nullable=True)
    UserId = Column(String(36), ForeignKey(UserRegDM.SysId), nullable=False)
    User = relationship(UserRegDM, backref=backref("UserReg"))