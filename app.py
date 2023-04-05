# This contains the code as well as the index for the api

# 1. Importing Necessary modules
import pickle

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from patient_data import patientData

# 2. Declaring our FastAPI instance/ Create the app object
app = FastAPI()
pickle_in = open("trained_model-2.0.0.pkl", "rb")
classifier = pickle.load(pickle_in)

# CORS headers
origins = ["http://localhost",
           "http://localhost:8080",
           "https://myapp.herokuapp.com",
           "http://www.e-hospital.ca/alzheimersPrediction",
           "http://www.e-hospital.ca",
           "http://localhost:5000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 3. Defining path operation for root endpoint. Opens at http://127.0.0.1:8000/
@app.get('/')
def main():
    return {'message': 'Welcome to our Project!'}


# 4. Defining path operation for /name endpoint. Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def hello_name(name: str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to our Project!, {name}'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted diagnosis with the confidence
@app.post('/predict')
def predict_disease(data: patientData):
    data = data.dict()  # 11 inputs
    visit = data['Visit']
    mr_delay = data['MR_Delay']
    m_f = data['M_F']
    age = data['Age']
    educ = data['EDUC']
    ses = data['SES']
    mmse = data['MMSE']
    cdr = data['CDR']
    etiv = data['eTIV']
    nwbv = data['nWBV']
    asf = data['ASF']

    # print(random_forest_model.predict([[inputs...]]))
    # the model takes the inputs passed through the api
    nondemented = 0
    demented = 0
    for i in range(50):
        prediction: object = classifier.predict([[visit, mr_delay, m_f, age, educ, ses, mmse, cdr, etiv, nwbv, asf]])
        if prediction[0] > 0.5:
            nondemented = nondemented + 1
        else:
            demented = demented + 1
    print(nondemented)
    print(demented)
    # If prediction = 0 then patient is Demented and if prediction = 1, patient is Nondemented
    if nondemented > demented:
        predictions = "Nondemented!"
        percentage = demented / 50 * 100
    else:
        predictions = "Demented!"
        percentage = demented / 50 * 100
    return {
        'prediction': predictions,
        'percentage': str(percentage)
    }


# 6. Run the API with uvicorn. Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# To run the API, first change the directory to the current project then use the command,
# uvicorn app:app --reload
# Then use swagger through http://127.0.0.1:8000/docs
