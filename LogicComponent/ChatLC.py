import uuid
from Config import Config
import openai

from DataModels.UserHistoryDM import UserHistoryDM

# Load your API key from an environment variable or secret management service
# openai.api_key = "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"
# Question = "What is Current time of Dubai?"
# UserId = '9a11d78e-899a-4299-98b4-eaeb86498a46'
def GetAnswer(UserId,Question):
    Session = Config.Session
    openai.api_key = Config.API_KEY
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
    data =  UserHistoryDM(
                SysId=str(uuid.uuid4()),
                Question=Question,
                Answer=answer,
                UserId = UserId
                )

    Session.add(data)
    Session.commit()
    #Session.close()
    return "Success",answer