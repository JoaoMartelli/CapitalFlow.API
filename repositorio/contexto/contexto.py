from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

contexto = create_engine('mssql+pyodbc://JOÃOMARTELLI\\SQLEXPRESS/CapitalFlow?trusted_connection=yes&TrustServerCertificate=yes&driver=ODBC+Driver+17+for+SQL+Server')
Session = sessionmaker(bind=contexto)
session = Session()

Base = declarative_base()