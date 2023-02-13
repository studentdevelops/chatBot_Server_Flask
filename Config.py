from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from DataModels.BaseDM import Base
from DataModels.UserDM import UserDM
from DataModels.UserKeyDM import UserKeyDM
from DataModels.UserHistoryDM import UserHistoryDM
class Config:
    engine = create_engine('mssql+pyodbc://' + 'LAPTOP-LC07V53A/CPING?' + 'driver=SQL+Server+Native+Client+11.0')
    Session = sessionmaker(bind=engine)
    Session = Session()
    API_KEY  = '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'
    Base = Base.metadata.create_all(engine)

