import uuid

import pandas as pd
from flask import Flask, request, jsonify
from LogicComponent.Prediction import Predict
from LogicComponent.UserReg_Log import CreateUser, ReturnUser
from LogicComponent.ChatLC import GetAnswer
from LogicComponent.AppHelper import Session as Sess
from LogicComponent.AppHelper import engine as eng

from sqlalchemy import update, text
from DataModels.UserDM import User

app = Flask(__name__)


@app.route('/post_data', methods=['POST'])
def post_data():
    # print('Call HEre')
    data = request.get_json(force=True)
    # print(data)
    try:
        df = pd.DataFrame(data, index=[0])
        df1 = df
        usysid = [str(uuid.uuid4()) for _ in range(len(df1))]
        df1.set_index(pd.Index(usysid, name='SysId'), inplace=True)
        df1.to_sql("users", con=eng, if_exists='append', chunksize=50)
        df = df.drop(['UserId', 'name', 'height',
                     'weight', 'surgery','bmr'], axis=1)
        userId = data['UserId']
        x = Predict(df)
        up = text(f"update users set medical_assistance='{x[0]}' where 'UserId'='{userId}'".strip())
        Sess.execute(up)
        Sess.commit()
        if (x == 1):
            return {'success': True, 'output': 1}
        else:
            return {'success': True, 'output': 0}
    except Exception as e:
        return {'success': False, "exception": str(e)}
    finally:
        Sess.close()


@app.route('/Get_Answer', methods=['POST'])
def Get_Answer():
    data = request.get_json(force=True)
    print(data)
    try:
        Question = data['Question']
        UserId = data['UserId']
        status, answer = GetAnswer(Question=Question, UserId=UserId)
        # print(status,answer)
        return {'success': status, 'message': answer}
    except Exception as e:
        print(e)
        return {'success': False, "exception": e}
    finally:
        Sess.close()


@app.route('/Create_User', methods=['POST'])
def Create_User():
    data = request.get_json(force=True)
    # print(data)
    try:
        email = data['email']
        password = data['password']
        return CreateUser(email, password)
    except Exception as e:
        return {'success': 'false'}
    finally:
        Sess.close()


@app.route('/Get_User', methods=['POST'])
def Get_User():
    data = request.get_json(force=True)
    try:
        email = data['email']
        password = data['password']
        return ReturnUser(email, password)

    except Exception as e:
        print(e)
        return {'success': e}
    finally:
        Sess.close()


if __name__ == '__main__':
    app.run(debug=True)
