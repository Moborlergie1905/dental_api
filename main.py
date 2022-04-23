from fastapi import APIRouter, FastAPI
from database import conn
from models.index import patients
from schemas.patient import Patient

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/patients")
async def get_patients():   
    return conn.execute(patients.select()).fetchall() 
    
    
@app.post("/patients")
async def add_patient(patient: Patient):
    conn.execute(patients.insert().values(
        patientID=patient.patientID,
        pname=patient.pname,
        date_of_birth=patient.date_of_birth,
        paddress=patient.paddress,
        pphone=patient.pphone
    ))
    return conn.execute(patients.select()).fetchall() 

