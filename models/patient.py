from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from database import meta

patients = Table(
    'patient', meta,
    Column('patientID',Integer, primary_key=True),
    Column('pname', String(100)),
    Column('date_of_birth', String(15)),
    Column('paddress', String(225)),
    Column('pphone', String(15))
)

