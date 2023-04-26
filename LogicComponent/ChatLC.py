
from LogicComponent.AppHelper import Api_key as Api
from LogicComponent.AppHelper import Session as Sess
import openai
import uuid

from DataModels.UserHistoryDM import UserChatHistoryDM

# Load your API key from an environment variable or secret management service
# Question = "What is Current time of Dubai?"
# UserId = '9a11d78e-899a-4299-98b4-eaeb86498a46'
def GetAnswer(Question,UserId):
    Session = Sess
    openai.api_key = Api
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=Question,
    temperature=0.45,
    max_tokens=200,
    top_p=0,
    frequency_penalty=1,
    presence_penalty=0.0,
    best_of=2
    )
    answer = response.choices[0].text
    data =  UserChatHistoryDM(
                SysId = str(uuid.uuid4()),
                Question=Question,
                Answer=answer,
                UserId = UserId
                )

    Session.add(data)
    Session.commit()
    #Session.close()
    return "true",answer
