
from DataModels import *
import os
from DataModels.BaseDM import Base
from DataModels.UserHistoryDM import UserChatHistoryDM
from DataModels.UserDM import User
from DataModels.UserRegDM import UserRegDM
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# engine = create_engine('mssql+pyodbc://' + 'LAPTOP-LC07V53A/CPING?' + 'driver=SQL+Server+Native+Client+11.0')
# engine = create_engine('sqlite:///Database/Test.db', echo=True)

engine = create_engine("postgresql://postgres:123@localhost:5432/test", echo=False )
connect = engine.connect()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session = Session()
Api_key = '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'
