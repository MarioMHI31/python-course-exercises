HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'MDSRMCA12@'
DATABASE = 'myfirstdb'
TABLE = 'masina'

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql
from urllib.parse import quote
#seMQGqFqu1BfBgPH6h5eiDY8JH9QJD-lYrzFzxAYRTM=
from cryptography.fernet import Fernet
key = b"seMQGqFqu1BfBgPH6h5eiDY8JH9QJD-lYrzFzxAYRTM="
cipher_suite = Fernet(key)
encrypted_password = cipher_suite.encrypt(PASSWORD.encode())
connection_string = f"mysql+pymysql://{USER}:{encrypted_password}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(connection_string)

Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

class Masina(Base):
    __tablename__ = TABLE

    id = Column(Integer, primary_key=True)
    marca = Column(String(100))
    model = Column(String(100))
    an = Column(Integer())
    combustibil = Column(String(100))

masinaunu = Masina(marca="BMW", model="seria 3", an=2022, combustibil="Benzina")
session.add(masinaunu)
session.commit()

limited_cars = session.query(Masina).limit(5).all()

for masina in limited_cars:
    print(f"ID: {masina.id}, marca: {masina.marca}, model: {masina.model}, an: {masina.an}, combustibil: {masina.combustibil}")
session.close()
