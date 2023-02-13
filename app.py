from flask import Flask,request
from Config import Config
from LogicComponent.ChatLC import GetAnswer
from LogicComponent.ApiKeyLC import ManageApiKey
app = Flask(__name__)

@app.route('/Home')
def index():
    return 'Hello, World!'

@app.route('/post_data', methods=['POST'])
def post_data():
    print('Call HEre')
    data = request.get_json()
    print(type(data))
    return 'Received data: {}'.format(data), 200

@app.route('/GetAnswer',methods = ['POST'])
def ReturnAnswer():
    print('Called IT')
    data = request.get_json()
    try:
        UserId = data['UserId']
        Question = data['Question']
        staus,answer=GetAnswer(UserId=UserId,Question=Question)
        return {'Status':staus,'Answer':answer}
    except Exception as e:
        print(e)
        return {'Status':'Error'}
    finally:
        Config.Session.close()
@app.route('/ApiKey',methods=['POST'])
def ApiKey():
    print('Called ApiKey')
    data = request.get_json()
    try:
        actiontype = data['actiontype']
        UserId = data['UserId']
        Question = data['Question']
        ApiKey = data['ApiKey']
        result = ManageApiKey(actiontype=actiontype,UserId=UserId,Question=Question,ApiKey=ApiKey)
        return result
    except Exception as e:
        print(e)
        return {'Status':'error'}
    finally:
        Config.Session.close()
if __name__ == '__main__':
    app.run(debug=True)
