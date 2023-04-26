
from DataModels import *

import os
from dotenv import load_dotenv

from DataModels.BaseDM import Base
from DataModels.UserHistoryDM import UserChatHistoryDM
from DataModels.UserDM import User
from DataModels.UserRegDM import UserRegDM
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

# engine = create_engine('mssql+pyodbc://' + 'LAPTOP-LC07V53A/CPING?' + 'driver=SQL+Server+Native+Client+11.0')
# engine = create_engine('sqlite:///Database/Test.db', echo=True)

postgresUrl = os.getenv("POSTGRESURL")
engine = create_engine(postgresUrl, echo=False)
connect = engine.connect()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session = Session()
Api_key = os.getenv("API_KEY")
