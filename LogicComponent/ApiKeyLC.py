import uuid
from enum import  Enum
from DataModels.UserKeyDM import UserKeyDM
from Config import Config
from LogicComponent.ChatLC import GetAnswer


class ActionType(Enum):
    CREATE = 1
    READ = 2
    DELETE = 3

def ManageApiKey(UserId,ApiKey,actiontype,Question):
    Session = Config.Session
    UserId = str(UserId)
    actiontype =  int(actiontype)
    apikey = str(ApiKey)
    if (ActionType(actiontype) == ActionType.CREATE and (UserId != None or UserId != "")):
        print('Create API and Return Key set count =0')
        apikey = str(uuid.uuid4())
        query = Session.query(UserKeyDM).filter(UserKeyDM.UserId == UserId).first()
        if query is None:
            data = UserKeyDM(
                SysId =  apikey,
                TotalRequests = 0,
                UserId = UserId,
                )
            Session.add(data)
            Session.commit()
            Session.close()
            return {"Status":"Success","Message":apikey}
        else :
            return {"Status":"Error","Message":'Api Key Already Generated'}
    elif(ActionType(actiontype) ==  ActionType.READ and (apikey!= None or apikey != "") and (UserId != None or UserId != "")):
        print('Read API Key and Return Call Chat LC and Increase Count by 1')
        query = Session.query(UserKeyDM).filter(UserKeyDM.SysId == ApiKey , UserKeyDM.UserId==UserId).first()
        print(Question is not None and Question!="")
        if query is not None and (Question is not None and Question!=""):
            print('Api Successful connection .. ask Question')
            Status,Answer=GetAnswer(UserId,Question)
            Session = Config.Session
            query.TotalRequests+=1
            Session.commit()
           #  Session.close()
            return {"Status":Status, "Message": Answer}
        else:
            print('please generate API Key Or No Question Provided')
            return {"Status": "Error", "Message":'please generate API Key Or No Question Provided' }
    elif (ActionType(actiontype) == ActionType.DELETE and (UserId != None or UserId != "")):
        print('Delete Value and Return True or False')
        query = Session.query(UserKeyDM).filter(UserKeyDM.SysId == ApiKey, UserKeyDM.UserId == UserId).first()
        if query is not None:
            Session.delete(query)
            Session.commit()
            Session.close()
            return {"Status":"Success","Message":'Deleted'}
        else:
            print('Not Found')
            return {"Status": "Error", "Message": 'Not Found'}
    else:
        print('Some Error has Ocurred plaese check values sent to')
        return {"Status": "Success", "Message": 'Error101'}
