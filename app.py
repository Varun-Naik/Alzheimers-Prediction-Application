# 1. Importing Necessary modules
from fastapi import FastAPI
from patient_data import patientData
import uvicorn
import numpy as np
import pickle
import pandas as pd

# 2. Declaring our FastAPI instance/ Create the app object
app = FastAPI()
pickle_in = open("trained_model-0.1.0.pkl", "rb")
classifier = pickle.load(pickle_in)


# 3. Defining path operation for root endpoint. Opens at http://127.0.0.1:8000/
@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}


# 4. Defining path operation for /name endpoint. Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def hello_name(name: str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to GeeksforGeeks!, {name}'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted diagnosis with the confidence
@app.post('/predict')
def predict_disease(data: patientData):
    data = data.dict()
    visit = data['Visit']
    mr_delay = data['MR_Delay']
    m_f = data['M_F']
    hand = data['Hand']
    age = data['Age']
    educ = data['EDUC']
    ses = data['SES']
    mmse = data['MMSE']
    cdr = data['CDR']
    etiv = data['eTIV']
    nwbv = data['nWBV']
    asf = data['ASF']

    # print(random_forest_model.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])


# 6. Run the API with uvicorn. Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
# uvicorn main:app --reload
