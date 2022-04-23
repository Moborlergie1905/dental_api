from typing import List
from sqlalchemy.orm import Session
from models import Patient
from schemas import CreatePatient

def get_all_patients(session: Session) -> List[Patient]:
    return session.query(Patient).all()

def create_patient(session: Session, info_patient: CreatePatient) -> Patient:
    new_patient = Patient(**info_patient.dict())
    session.add(new_patient)
    session.commit()
    session.refresh(new_patient)
    return new_patient