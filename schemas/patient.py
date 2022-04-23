from pydantic import BaseModel

class Patient(BaseModel):
    patientID: int
    pname: str
    date_of_birth: str
    paddress: str
    pphone: str