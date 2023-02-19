# File to create a structure for the input to the ML model
# This way the attributes of the class patientData can be used as features of the data.

from pydantic import BaseModel


# Class which describes patient data measurements
# Contains 11 attibutes/inputs
class patientData(BaseModel):
    Visit: int
    MR_Delay: int
    M_F: int
    Age:int
    EDUC: int
    SES: float
    MMSE: float
    CDR: float
    eTIV: int
    nWBV: float
    ASF: float
