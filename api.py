from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_all_patients, create_patient
from database import get_db
from schemas import Patient, CreatePatient

router = APIRouter()

class Patients:
    Session: Session = Depends(get_db)
    
    def list_patients(self):
        patients_list = get_all_patients(self.Session)
        response = {"data": patients_list}
        
        return response
    
    def add_patient(self, pat_info: CreatePatient):
        pat_info = create_patient(self.Session, pat_info)
        return pat_info
    