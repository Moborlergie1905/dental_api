from sqlalchemy import create_engine,MetaData

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Oyinromola2405@localhost:3306/project_dental"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://sql5487505:FGtbw2kj9x@sql5.freemysqlhosting.net:3306/sql5487505"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

meta = MetaData()

conn = engine.connect()
