from DataModels.UserDM import User
#from AppHelper import Session
import os
import numpy as np
import joblib
def Predict(values):
    try:
        model_path = os.path.join('MLMODELS', "rfc_model.pkl")
        # Load the trained model from disk
        loaded_model = joblib.load(model_path)
        pred = loaded_model.predict(values)
        return pred
    except Exception as e:
        return {"Fail":e}

# l=[30.89, 58.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 19.0, 1.0]
# nd = np.array(l).reshape(1,-1)
# p=Predict(nd)
# print(p)