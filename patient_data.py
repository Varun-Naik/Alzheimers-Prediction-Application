# File to create a structure for the input to the ML model

from pydantic import BaseModel


# Class which describes patient data measurements
class patientData(BaseModel):
    Visit: int
    MR_Delay: int
    M_F: int
    Hand: int
    Age:int
    EDUC: int
    SES: float
    MMSE: float
    CDR: float
    eTIV: int
    nWBV: float
    ASF: float
